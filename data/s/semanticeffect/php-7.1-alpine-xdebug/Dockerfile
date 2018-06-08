FROM php:7.1-fpm-alpine  
  
ARG BUILD_DATE  
ARG VCS_REF  
ENV COMPOSER_ALLOW_SUPERUSER 1  
  
LABEL Maintainer="Varr Willis <semanticeffect@gmail.com>" \  
Description="PHP 7.1 container based on alpine with xDebug enabled & composer
installed." \  
org.label-schema.name="php-7.1-alpine-xdebug" \  
org.label-schema.description="PHP 7.1 container based on alpine with xDebug
enabled & composer installed." \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/varrwillis/php-7.1-alpine-
xdebug.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0"  
  
RUN apk update \  
&& apk add --no-cache git mysql-client curl openssh-client icu libpng libjpeg-
turbo libmcrypt libmcrypt-dev \  
&& apk add --no-cache --virtual build-dependencies icu-dev \  
libxml2-dev freetype-dev libpng-dev libjpeg-turbo-dev g++ make autoconf \  
&& docker-php-source extract \  
&& pecl install xdebug redis \  
&& docker-php-ext-enable xdebug redis \  
&& docker-php-source delete \  
&& docker-php-ext-install mcrypt pdo_mysql soap intl zip \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& apk del build-dependencies \  
&& apk del libmcrypt-dev \  
&& rm -rf /tmp/*  
  
# COPY php.ini /usr/local/etc/php/  
  
USER www-data  
  
WORKDIR /var/www  

