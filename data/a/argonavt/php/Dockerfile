FROM php:7.1-apache  
  
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y \  
&& apt-get install -y git libmcrypt-dev libpng12-dev libjpeg-dev libpq-dev
mysql-client curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install mcrypt gd mbstring pdo pdo_mysql zip mysqli \  
&& pecl install xdebug \  
&& rm -rf /tmp/pear  
  
RUN a2enmod rewrite  
  
ADD php.ini /usr/local/etc/php/  
  
ENV XDEBUGINI_PATH=/usr/local/etc/php/conf.d/xdebug.ini  
RUN echo "zend_extension="`find /usr/local/lib/php/extensions/ -iname
'xdebug.so'` > "$XDEBUGINI_PATH"  
COPY xdebug.ini /tmp/xdebug.ini  
RUN ( ( echo "xdebug.remote_host=" ; /sbin/ip route|awk '/default/ { print $3
}' ; ) | \  
tr "\n" " " ; echo "" ; ) >> /usr/local/etc/php/conf.d/xdebug.ini  
  
RUN cat /tmp/xdebug.ini >> $XDEBUGINI_PATH  
  
# Change uid and gid of apache to docker user uid/gid  
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data  
  
WORKDIR /var/www/html  

