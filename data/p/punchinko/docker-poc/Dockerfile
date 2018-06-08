FROM php:7.0.12-fpm  
  
COPY ./sources /tmp  
  
# Updating, Installing Tools  
RUN apt-get update \  
&& apt-get install -y \  
libmcrypt-dev \  
libpng12-dev \  
libssl-dev \  
libcurl4-gnutls-dev \  
libxml2 \  
wget \  
libxml2-dev \  
&& cd /tmp \  
&& pecl install redis-3.0.0.tgz \  
&& pecl install mongodb-1.1.9.tgz \  
&& pecl install msgpack-2.0.1.tgz \  
&& pecl install solr-2.4.0.tgz \  
&& pecl install xdebug-2.4.1.tgz \  
&& docker-php-ext-install mysqli pdo_mysql mcrypt opcache \  
&& docker-php-ext-enable redis \  
&& docker-php-ext-enable mongodb \  
&& docker-php-ext-enable msgpack \  
&& docker-php-ext-enable solr \  
&& docker-php-ext-enable xdebug \  
&& tar -xzf igbinary-2.0.0.tar.gz && cd igbinary-2.0.0 \  
&& phpize && ./configure && make && make install \  
&& docker-php-ext-enable igbinary \  
&& cd /tmp && tar -xzf cphalcon-3.0.1.tar.gz && cd cphalcon-3.0.1/build \  
&& ./install \  
&& docker-php-ext-enable phalcon \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& cd /etc/ \  
&& mkdir images \  
&& cd images \  
&& wget https://hub.docker.com/hub-static/img/nav/docker-logo-loggedin.png  

