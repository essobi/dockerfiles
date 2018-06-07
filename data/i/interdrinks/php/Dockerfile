FROM composer:latest as composer  
FROM php:7.1-fpm-alpine  
  
ENV APCU_VERSION 5.1.8  
# https://getcomposer.org/doc/03-cli.md#composer-allow-superuser  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV WKHTMLTOPDF_BINARY /usr/bin/wkhtmltopdf  
  
COPY --from=composer /usr/bin/composer /usr/bin/composer  
COPY php.ini /usr/local/etc/php/php.ini  
COPY php-fpm.conf /usr/local/etc/php-fpm.d/php-fpm.conf  
COPY wkhtmltopdf /usr/bin/wkhtmltopdf  
  
HEALTHCHECK --interval=10s \--timeout=3s \  
CMD \  
SCRIPT_NAME=/ping \  
SCRIPT_FILENAME=/ping \  
REQUEST_METHOD=GET \  
cgi-fcgi -bind -connect 127.0.0.1:9000 || exit 1  
  
WORKDIR /srv/api-platform  
  
RUN set -xe \  
&& apk add --no-cache --virtual .persistent-deps \  
git \  
icu-libs \  
zlib \  
fcgi \  
libgcc \  
libstdc++ \  
libx11 \  
glib \  
libxrender \  
libxext \  
libintl \  
libcrypto1.0 \  
libssl1.0 \  
ttf-dejavu \  
ttf-droid \  
ttf-freefont \  
ttf-liberation \  
ttf-ubuntu-font-family \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
icu-dev \  
zlib-dev \  
libxml2-dev \  
&& docker-php-ext-install \  
intl \  
pdo_mysql \  
zip \  
soap \  
&& pecl install \  
apcu-${APCU_VERSION} \  
redis \  
&& docker-php-ext-enable \  
apcu \  
opcache \  
redis \  
&& rm -rf /tmp/pear \  
&& apk del .build-deps \  
&& composer global require "hirak/prestissimo:^0.3" \--prefer-dist --no-
progress --no-suggest --optimize-autoloader --classmap-authoritative \  
&& composer clear-cache \  
&& mkdir -p var/cache var/logs \  
&& chmod -R 777 var /tmp  
  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/alpine/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
CMD ["php-fpm"]  

