FROM php:fpm-alpine  
  
RUN apk update && apk add --no-cache git postgresql-dev zip unzip zlib-dev g++
make autoconf libxslt-dev \  
&& docker-php-ext-install pdo_pgsql zip bcmath xsl  
  
RUN pecl install apcu  
RUN pecl install igbinary  
  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
RUN curl -sSL https://github.com/xdebug/xdebug/archive/4ada850.zip -o
/tmp/xdebug.zip \  
&& unzip /tmp/xdebug.zip -d /tmp \  
&& cd /tmp/xdebug-* \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /tmp/xdebug*  
  
RUN rm -rf /var/cache/apk/*  

