FROM vinaocruz/php-7:alpine  
  
RUN apk add --no-cache \  
\--virtual .phpize_deps \  
$PHPIZE_DEPS \  
libressl-dev  
  
RUN pecl install xdebug && \  
docker-php-ext-enable xdebug  
  
RUN apk del .phpize_deps  
  
ENV XDEBUG_INI_DIR /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
RUN echo "xdebug.remote_enable=on" >> $XDEBUG_INI_DIR \  
&& echo "xdebug.remote_autostart=off" >> $XDEBUG_INI_DIR \  
&& echo "xdebug.remote_port=9001" >> $XDEBUG_INI_DIR

