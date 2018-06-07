FROM php:7.0.27-fpm-alpine  
  
  
###Environments defaults  
ENV PHP_SESSION_SAVE_HANDLER files  
ENV PHP_SESSION_SAVE_PATH /tmp  
ENV PHP_OP_CACHE_ENABLE 1  
ENV PHP_OP_CACHE_REVALIDATE_FREQ 600  
ENV PHP_OP_CACHE_SAVE_COMMENTS 1  
ENV PHP_TIMEZONE UTC  
ENV PHP_CLEAR_ENV no  
ENV PHPREDIS_VERSION 3.1.4  
RUN mkdir -p /usr/src/php/ext/redis \  
&& curl -L
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz | tar
xvz -C /usr/src/php/ext/redis --strip 1 \  
&& echo 'redis' >> /usr/src/php-available-exts  
  
RUN apk upgrade --update \  
&& apk add --no-cache --virtual .build-deps \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
libmcrypt-dev \  
icu-dev \  
openssl-dev \  
krb5-dev \  
curl-dev \  
imap-dev \  
$PHPIZE_DEPS \  
&& pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug \  
&& echo "xdebug.idekey = IDEKEY" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.default_enable = 0" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_enable = 1" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_autostart = 0" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_connect_back = 0" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo "xdebug.profiler_enable = 0" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& docker-php-ext-install \  
iconv mcrypt mbstring mysqli pdo_mysql curl session zip intl opcache redis \  
&& docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install \  
gd \  
&& docker-php-ext-configure \  
imap --with-imap-ssl --with-kerberos \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
##CLEANUP  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add \--no-cache --virtual .php-rundeps $runDeps \  
&& apk del .phpize-deps-configure .build-deps \  
&& find / -type f -iname \\*.apk-new -delete \  
&& rm -rf /var/cache/apk/*  
  
COPY conf/php.ini /usr/local/etc/php/  
COPY conf/php-cli.ini /usr/local/etc/php/  
COPY conf/php-fpm.conf /usr/local/etc/  
COPY conf/www.conf /usr/local/etc/php-fpm.d/  
  
#Clear env directive correction  
RUN sed -i "s|clear_env\s*=\s*no|clear_env = $PHP_CLEAR_ENV|g"
/usr/local/etc/php-fpm.d/docker.conf \  
&& sed -i "s|clear_env\s*=\s*yes|clear_env = $PHP_CLEAR_ENV|g"
/usr/local/etc/php-fpm.d/www.conf  
  
#ports  
EXPOSE 9000  

