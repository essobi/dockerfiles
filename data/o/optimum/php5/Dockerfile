FROM php:5.6-fpm  
  
MAINTAINER optimum <info@optimum-web.com>  
  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
libpng++-dev\  
zlib1g-dev \  
htop \  
nmon \  
php5-apcu \  
&& docker-php-ext-install -j$(nproc) mcrypt zip pdo_mysql mysqli gd  
  
ADD ./dockerfiles/app/php.ini /usr/local/etc/php/php.ini  
  
RUN apt-get install -y zlib1g-dev \  
&& pecl install memcache \  
&& docker-php-ext-enable memcache gd mcrypt  
  
WORKDIR /app  
  
RUN curl -sS https://getcomposer.org/installer | php --  
RUN rm -rf /app/vendor/sepia/po-parser/.git  
  
ADD composer.json /app  
ADD composer.lock /app  
  
RUN php composer.phar install  
RUN php composer.phar update  
  
RUN ln -s /app /var/www/html/app  
  
# Add image configuration and scripts  
ADD run-new.sh /run-new.sh  
  
RUN chmod 755 /*.sh  
  
RUN /run-new.sh  

