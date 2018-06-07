FROM artemstd/debian-php:latest  
  
MAINTAINER artemstd <artemstd@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
# env  
ENV XDEBUGINI_PATH=/etc/php/${PHP_VERSION}/fpm/conf.d/xdebug.ini  
  
# php fpm  
RUN apt-get update && apt-get install -y php${PHP_VERSION}-fpm  
  
# configure php  
RUN sed -i "/;date.timezone /c date.timezone = ${TIMEZONE}"
$PHP_DIR/fpm/php.ini \  
&& sed -i "/^short_open_tag /c short_open_tag = On" $PHP_DIR/fpm/php.ini \  
&& sed -i "/^listen /c listen = 0.0.0.0:9000" $PHP_DIR/fpm/pool.d/www.conf \  
&& sed -i "/;daemonize /c daemonize = no" $PHP_DIR/fpm/php-fpm.conf  
  
RUN printf "xdebug.remote_autostart=0 \n\  
xdebug.default_enable = On \n\  
xdebug.var_display_max_depth=6 \n\  
xdebug.remote_enable=1 \n\  
xdebug.remote_host=xdebug \n\  
xdebug.remote_port=9904 \n\  
xdebug.remote_handler=dbgp \n\  
xdebug.idekey=PHPSTORM \n\  
xdebug.remote_log=/var/log/xdebug.log \n\  
xdebug.profiler_enable_trigger=1 \n\  
xdebug.profiler_enable=0 \n\  
xdebug.profiler_output_dir=/tmp/profiler \n\  
xdebug.show_local_vars=1 \n\  
xdebug.overload_var_dump=1 \n\  
xdebug.max_nesting_level = 250 \n" >> $XDEBUGINI_PATH  
  
RUN mkdir /run/php && chown -R www-data:www-data /var/www /run/php  
  
EXPOSE 9000  
ENTRYPOINT php-fpm${PHP_VERSION}  

