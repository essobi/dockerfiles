FROM php:7.0.8-fpm  
MAINTAINER Mark Shust <mark.shust@mageinferno.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
cron \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev  
  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/  
  
RUN docker-php-ext-install \  
gd \  
intl \  
mbstring \  
mcrypt \  
pdo_mysql \  
bcmath \  
soap \  
xsl \  
zip  
  
RUN docker-php-ext-install bcmath  
  
RUN curl -sS https://getcomposer.org/installer | \  
php -- \  
\--install-dir=/usr/local/bin \  
\--filename=composer \  
\--version=1.1.2  
  
RUN pecl install xdebug-beta && \  
docker-php-ext-enable xdebug  
  
RUN touch /usr/local/etc/php/conf.d/xdebug.ini  
RUN echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20151012/xdebug.so" >> /usr/local/etc/php/conf.d/xdebug.ini  
RUN echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/xdebug.ini  
RUN echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/xdebug.ini  
RUN echo "xdebug.remote_connect_back=1" >>
/usr/local/etc/php/conf.d/xdebug.ini  
RUN echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/xdebug.ini  
RUN echo "xdebug.scream=0" >> /usr/local/etc/php/conf.d/xdebug.ini  
RUN echo "xdebug.show_local_vars=1" >> /usr/local/etc/php/conf.d/xdebug.ini  
RUN echo "xdebug.idekey=PHPSTORM" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
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
  
WORKDIR /srv/www  
  
CMD ["/usr/local/bin/start"]  

