FROM profideo/php-7.2-fpm  
  
# Install PHP extensions  
RUN apt-get update && apt-get install -y \  
libbz2-dev \  
libicu-dev \  
wget \  
zlib1g-dev \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-configure opcache --enable-opcache --enable-opcache-file \  
&& docker-php-ext-install bz2 intl opcache pdo pdo_mysql zip  
  
# PHP configuration  
COPY files/www.conf /usr/local/etc/php-fpm.d/www.conf  
COPY files/opcache.ini $PHP_INI_DIR/conf.d/  
RUN mkdir /home/profideo/.opcache && chown -R profideo:profideo
/home/profideo/.opcache  
  
# Configure logstash-forwarder  
RUN echo 'deb http://packages.elastic.co/logstashforwarder/debian stable main'
| tee /etc/apt/sources.list.d/logstashforwarder.list  
RUN wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add
-  
RUN apt-get -qq update && apt-get install logstash-forwarder  
RUN mkdir -p /etc/pki/tls/certs  
COPY files/logstash-forwarder.crt /etc/pki/tls/certs/logstash-forwarder.crt  
RUN chown profideo:profideo /etc  
  
# Node  
RUN apt-get update && apt-get install -y curl python-software-properties  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get update && apt-get install -y nodejs  
RUN mkdir -p /home/profideo/.npm  
RUN chown -R profideo /home/profideo/.npm  
RUN npm install -g less  
RUN npm install -g bower  
  
# Nginx configuration  
COPY files/nginx.conf /etc/nginx/nginx.conf  
  
# Supervisor  
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]  

