FROM 8select/php-fpm:0.4.1  
MAINTAINER Andreas Kleiber <andreas.kleiber@8select.de>  
  
ENV XDEBUG_VERSION 2.4.0RC4  
  
RUN pecl install xdebug-${XDEBUG_VERSION}  
RUN docker-php-ext-enable xdebug  
RUN echo xdebug.remote_enable=1 >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini; \  
echo xdebug.remote_autostart=0 >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini; \  
echo xdebug.remote_connect_back=1 >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini; \  
echo xdebug.remote_port=9001 >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini;  

