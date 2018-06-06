FROM cubicmushroom/php:7.0-fpm  
MAINTAINER Toby Griffiths <toby@cubicmushroom.co.uk>  
  
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y  
  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
  
RUN sed -i '1 a xdebug.remote_autostart=1' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_mode=req' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_handler=dbgp' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_port=9000' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_host=10.254.254.254'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_enable=1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_log=/tmp/xdebug.log'
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
RUN touch /tmp/xdebug.log && chmod 666 /tmp/xdebug.log

