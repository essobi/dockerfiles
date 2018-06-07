FROM php:7.2-fpm-alpine  
  
RUN apk add --no-cache libpng-dev libmcrypt-dev bash autoconf build-base \  
&& docker-php-ext-install gd mysqli pdo_mysql bcmath opcache \  
&& pecl install redis \  
&& pecl install xdebug \  
&& pecl install swoole \  
&& pecl install channel://pecl.php.net/mcrypt-1.0.1 \  
&& apk del build-base autoconf  
  
RUN echo "export TERM=xterm" >> /root/.bashrc \  
&& rm -rf /usr/local/etc/php-fpm.conf \  
&& mkdir /php \  
&& ln -s /php/php.ini /usr/local/etc/php/php.ini \  
&& ln -s /php/php-fpm.conf /usr/local/etc/php-fpm.conf  
  
WORKDIR /www  
  
CMD php-fpm  

