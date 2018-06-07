FROM wordpress:4.9-php7.0-apache  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y \  
libpng-dev \  
libjpeg-dev \  
libxml2-dev \  
libmcrypt-dev \  
libmhash2 \  
libc6 \  
zlib1g \  
bzip2 \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install -j$(nproc) opcache mcrypt soap \  
&& docker-php-ext-configure gd --with-png-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN pecl install xdebug-2.5.5 \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.default_enable = 1" >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable = 1" >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart = 1" >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.idekey = phpstorm" >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.remote_connect_back = 0" >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.profiler_enable = 0" >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.remote_host = 10.254.254.254" >>
$PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.remote_port = 9000" >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& docker-php-ext-enable xdebug  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]

