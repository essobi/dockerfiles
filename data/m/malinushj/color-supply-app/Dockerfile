FROM php:7.1-fpm-alpine  
  
COPY . /var/www  
  
RUN chown -R www-data /var/www/storage  
  
RUN apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
curl-dev \  
libmcrypt-dev \  
libtool \  
libxml2-dev \  
&& apk add --no-cache \  
curl \  
libmcrypt \  
mysql-client \  
&& docker-php-ext-install \  
curl \  
iconv \  
mbstring \  
mcrypt \  
pdo \  
pdo_mysql \  
pcntl \  
tokenizer \  
xml \  
zip \  
&& curl -s https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin/ --filename=composer \  
&& apk del -f .build-deps  
  
#####################################  
# xDebug:  
#####################################  
  
ARG INSTALL_XDEBUG=false  
RUN if [ ${INSTALL_XDEBUG} = true ]; then \  
# Install the xdebug extension  
pecl install xdebug && \  
docker-php-ext-enable xdebug \  
;fi  
  
# Copy xdebug configuration for remote debugging  
COPY ./docker/php-fpm/xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
  
COPY ./docker/php-fpm/laravel.ini /usr/local/etc/php/conf.d  
  
WORKDIR /var/www  
  
VOLUME /var/www

