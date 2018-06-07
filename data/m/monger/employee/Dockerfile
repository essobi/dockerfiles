FROM ubuntu:16.04  
# fix the bash  
RUN ln -snf /bin/bash /bin/sh  
  
# Install packages  
RUN apt-get update && apt-get install -my \  
vim \  
supervisor \  
curl \  
wget \  
git \  
zip \  
bzip2 \  
php7.0-bcmath \  
php7.0-cli \  
php7.0-curl \  
php7.0-fpm \  
php7.0-gd \  
php7.0-mcrypt \  
php7.0-mbstring \  
php7.0-mysqlnd \  
php7.0-soap \  
php7.0-xml \  
php7.0-zip \  
php7.0-bcmath  
  
# Remove unused packages  
RUN apt-get autoremove -y  
  
# Add some color to vim  
RUN printf "color desert" > /root/.vimrc  
  
# Add configuration files  
COPY conf/supervisord.conf /etc/supervisor/conf.d/  
COPY conf/php.ini /etc/php/7.0/fpm/conf.d/40-custom.ini  
COPY conf/php-fpm-www.conf /etc/php/7.0/fpm/pool.d/www.conf  
  
# Get Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Get PhantomJS  
WORKDIR /usr/local/share  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2  
RUN tar xjf phantomjs-1.9.7-linux-x86_64.tar.bz2  
RUN ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs
/usr/local/share/phantomjs  
RUN ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs  
RUN ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs
/usr/bin/phantomjs  
WORKDIR /  
  
# Pass all docker environment variables to php  
RUN sed -i '/^;clear_env = no/s/^;//' /etc/php/7.0/fpm/pool.d/www.conf  
  
# Initialize the PHP FPM pid file so Supervisor can find it  
RUN service php7.0-fpm start  
  
# Move the start file  
COPY start.sh /bin/original_start.sh  
RUN tr -d '\r' < /bin/original_start.sh > /bin/start.sh  
RUN chmod -R 700 /bin/start.sh  
  
EXPOSE 9000  
ENV TERM xterm  
  
CMD ["sh", "/bin/start.sh"]

