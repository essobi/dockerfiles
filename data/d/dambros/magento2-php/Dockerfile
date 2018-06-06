FROM php:7.0-fpm  
MAINTAINER Mario D Ambros <mdambros@lua.net>  
  
RUN apt-get update \  
&& apt-get install -y \  
cron \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
zip \  
vim  
  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/  
  
RUN docker-php-ext-install \  
bcmath \  
gd \  
intl \  
mbstring \  
mcrypt \  
pdo_mysql \  
soap \  
xsl \  
zip  
  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer  
  
RUN if [ 1 -eq "1" ]; then \  
yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_port=9089" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini;
\  
fi  
  
ENV PHP_MEMORY_LIMIT 2G  
ENV PHP_PORT 9000  
ENV PHP_PM dynamic  
ENV PHP_PM_MAX_CHILDREN 10  
ENV PHP_PM_START_SERVERS 4  
ENV PHP_PM_MIN_SPARE_SERVERS 2  
ENV PHP_PM_MAX_SPARE_SERVERS 6  
ENV APP_MAGE_MODE default  
  
COPY conf/www.conf /usr/local/etc/php-fpm.d/  
COPY conf/php.ini /usr/local/etc/php/  
COPY conf/php-fpm.conf /usr/local/etc/  
COPY bin/* /usr/local/bin/  
  
WORKDIR /var/www/html  
  
CMD ["/usr/local/bin/start"]  

