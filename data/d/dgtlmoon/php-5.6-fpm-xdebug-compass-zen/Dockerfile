FROM php:5.6-fpm  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libpq-dev \  
apt-utils \  
mysql-client \  
zlib1g-dev \  
drush  
  
RUN docker-php-ext-install pdo_mysql mbstring opcache \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd && apt-get install -y libmemcached-dev \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached  
  
# Any more gem's should only be installed through bundler  
RUN apt-get install ruby-full -y && gem update && gem install sass && gem
install bundler  
RUN apt-get install libgmp-dev -y  
  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& sed -i '1 a xdebug.remote_autostart=true' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_mode=req' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_handler=dbgp' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_connect_back=1 '
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_port=9000' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_host=127.0.0.1' /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& sed -i '1 a xdebug.remote_enable=1' /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  
  
ADD entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["php-fpm"]  

