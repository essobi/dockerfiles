FROM senasi/php:7.0  
RUN apk add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS && \  
pecl install xdebug && \  
docker-php-ext-enable xdebug && \  
apk del .phpize-deps-configure && \  
set -ex && \  
cd /usr/local/etc && \  
{ \  
echo '[Xdebug]'; \  
echo 'xdebug.remote_connect_back = 1'; \  
echo 'xdebug.remote_enable = 1'; \  
echo 'xdebug.profiler_enable_trigger = 1'; \  
echo 'xdebug.profiler_output_dir=/data/log'; \  
} | tee php/conf.d/xdebug.ini  
  

