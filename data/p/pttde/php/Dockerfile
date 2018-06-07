FROM php:7.2-fpm-alpine3.7  
MAINTAINER Linus Lotz<l.lotz@reply.de>  
ENV RUN_DEPS="bash icu-libs libgd libintl mariadb-client-libs postgresql-libs"  
ENV BUILD_DEPS="${PHPIZE_DEPS} freetype-dev icu-dev libjpeg-turbo-dev libpng-
dev libwebp-dev libxpm-dev mariadb-dev postgresql-dev zlib-dev"  
ENV PECL_EXTS="redis"  
ENV PHP_EXTS="gd intl mysqli opcache pdo_mysql pdo_pgsql zip"  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache $RUN_DEPS \  
&& apk add -t .build-deps $BUILD_DEPS \  
&& docker-php-ext-install $PHP_EXTS \  
&& pecl install -o -f $PECL_EXTS \  
&& docker-php-ext-enable $PECL_EXTS \  
&& apk del .build-deps \  
# Clear  
&& rm -rf /tmp/* /var/cache/apk/*  

