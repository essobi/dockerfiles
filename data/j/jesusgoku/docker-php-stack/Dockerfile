FROM tutum/lamp:latest  
MAINTAINER Jesús Urrutia <jesus.urrutia@gmail.com>  
# Enable new sources  
COPY config/sources.list /etc/apt/sources.list  
# Install Git  
RUN apt-get update && apt-get install -y curl  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
# Install Node and Npm  
RUN apt-get update && apt-get install -y nodejs npm  
# Install PHP extensions  
RUN apt-get update && apt-get install -y \  
php5-sqlite \  
php5-curl \  
php5-gd \  
php5-ldap \  
php5-imagick \  
php5-intl \  
php5-mongo \  
php5-redis \  
php5-pgsql  
RUN npm -g install bower  
RUN npm -g install pm2  
# For Web application  
EXPOSE 80  
EXPOSE 3306  
EXPOSE 8080  
# For terminal  
COPY tty/package.json /terminal/  
COPY tty/server.key /terminal/  
COPY tty/server.crt /terminal/  
COPY tty/index.js /terminal/  
# Make shortcut for nodejs  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
# Install terminal dependencies  
RUN cd /terminal && npm install  
# Copy supervisor files for run terminal  
COPY start-terminal.sh /start-terminal.sh  
COPY supervisord-terminal.conf /etc/supervisor/conf.d/supervisord-
terminal.conf  
RUN chmod 755 /start-terminal.sh  
# Apache configuration  
COPY config/apache_default.conf /etc/apache2/sites-available/000-default.conf  
COPY config/apache_symfony.conf /etc/apache2/conf-
available/apache_symfony.conf  
COPY config/apache_silex.conf /etc/apache2/conf-available/apache_silex.conf  
# Copy container initialization script  
COPY entrypoint.sh /  
WORKDIR /  
CMD ["bash", "/entrypoint.sh"]

