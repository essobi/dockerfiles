FROM ozconseil/php:7.2-varnish  
MAINTAINER ozconseil <dev@ozconseil.com>  
  
COPY apache2-foreground /usr/local/bin/  
  
COPY xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
RUN pecl install xdebug && docker-php-ext-enable xdebug  

