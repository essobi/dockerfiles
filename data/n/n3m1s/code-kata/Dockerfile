FROM php:7.1.3-fpm-alpine  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN if [ ${PHP_TIMEZONE} ]; then \  
echo "date.timezone=${PHP_TIMEZONE}" > $PHP_INI_DIR/conf.d/date_timezone.ini \  
;fi  
  
RUN docker-php-source extract \  
&& apk add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& apk del .phpize-deps-configure \  
&& docker-php-source delete \  
&& apk add --update --no-cache autoconf g++ imagemagick-dev libtool make \  
&& apk del autoconf g++ libtool make \  
&& apk add --update --no-cache \  
git \  
freetype-dev \  
libpng-dev libjpeg-turbo-dev \  
libmcrypt-dev \  
libintl icu icu-dev libxml2-dev \  
&& docker-php-ext-install intl zip soap pdo pdo_mysql opcache \  
&& docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" gd iconv mcrypt
bcmath  
  
# Install Code Sniffer  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/bin \  
\--filename=composer \  
&& composer global require "squizlabs/php_codesniffer=*"  
  
COPY ./xdebug.ini /usr/local/etc/php/conf.d/  
COPY ./opcache.ini /usr/local/etc/php/conf.d/  
COPY ./custom.ini /usr/local/etc/php/conf.d/  
  
WORKDIR /opt/project  
  
RUN rm -rf /var/cache/apk/*  
  
CMD ["php-fpm"]  

