FROM php:7.1-fpm-alpine  
  
ENV TZ="Europe/Berlin" \  
CODE_DIR="/code" \  
PUBLIC_DIR="/code/public"  
# Add production configuration from https://raw.githubusercontent.com/php/php-
src/PHP-7.1/php.ini-production  
COPY php.ini /usr/local/etc/php/php.ini  
# Add recommended opcache settings from
https://secure.php.net/manual/en/opcache.installation.php  
COPY opcache-recommended.ini /usr/local/etc/php/conf.d/opcache-recommended.ini  
COPY typo3.ini /usr/local/etc/php/conf.d/typo3.ini  
COPY docker-php-for-typo3-entrypoint.sh /usr/local/bin/docker-php-for-
typo3-entrypoint.sh  
  
RUN set -xe \  
&& apk add --no-cache --virtual .phpize-deps $PHPIZE_DEPS freetype-dev libtool
libjpeg-turbo-dev libpng-dev \  
&& export CFLAGS="$PHP_CFLAGS" CPPFLAGS="$PHP_CPPFLAGS" LDFLAGS="$PHP_LDFLAGS"
\  
&& pecl install apcu \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr \  
\--with-png-dir=/usr \  
\--with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysqli opcache zip \  
&& docker-php-ext-enable apcu \  
&& apk del .phpize-deps \  
&& apk add --no-cache imagemagick bash nano tzdata \  
&& chmod +x /usr/local/bin/docker-php-for-typo3-entrypoint.sh  
  
WORKDIR $CODE_DIR  
  
ENTRYPOINT ["docker-php-for-typo3-entrypoint.sh"]  
  
CMD ["php-fpm"]

