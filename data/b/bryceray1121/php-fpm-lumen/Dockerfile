FROM php:5.6-fpm  
  
MAINTAINER "Daniel Lapres" <dlapres@rxsavingsllc.com>  
  
# Install PHP-FPM and popular/laravel required extensions  
RUN apt-get update -y && \  
apt-get install -y \  
php5-xdebug  
  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install pdo_mysql  
  
# Install Memcache PHP Extension  
RUN apt-get install -y zlib1g-dev libmemcached-dev  
ADD https://pecl.php.net/get/memcached-2.2.0.tgz
/usr/src/php/ext/memcached.tgz  
RUN tar -xf /usr/src/php/ext/memcached.tgz -C /usr/src/php/ext/ && \  
rm /usr/src/php/ext/memcached.tgz && \  
docker-php-ext-install memcached-2.2.0  
  
COPY bin /usr/local/bin/  
COPY config/php.ini /usr/local/etc/php/php.ini  
COPY config/php-fpm.conf /usr/local/etc/php-fpm.conf  
  
RUN chmod u+x /usr/local/bin/docker-php-pecl-install  
  
# Setup for file system permissions on OSX  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  
  
RUN mkdir -p /data/log  
RUN chmod go+rw /data/log  
  
RUN chmod u+x /usr/local/bin/startup.sh  
CMD /usr/local/bin/startup.sh  

