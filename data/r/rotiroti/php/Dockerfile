FROM php:5.6-alpine  
  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache bash \  
&& apk add --no-cache --virtual build-dependencies g++ make autoconf \  
&& docker-php-source extract \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& docker-php-source delete \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& apk del build-dependencies \  
&& rm -fr /tmp/*  
  
COPY . /app  
WORKDIR /app  
  
CMD [ "php" ]  

