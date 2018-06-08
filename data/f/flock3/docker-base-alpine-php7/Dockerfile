FROM php:7.1-fpm-alpine  
LABEL maintainer = "infinityworks"  
  
RUN set -xe \  
&& printf "\n%s\n%s" "@edge http://dl-cdn.alpinelinux.org/alpine/edge/main" \  
"@community http://dl-cdn.alpinelinux.org/alpine/edge/community" \  
"@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" \  
>> /etc/apk/repositories \  
&& apk upgrade --no-cache apk-tools@edge \  
&& apk add --no-cache git nginx sed libressl@edge \  
logrotate exiftool libintl@edge tzdata \  
icu gmp@community gettext unzip@edge gnu-libiconv@testing \  
&& update-ca-certificates 2>/dev/null || true  
  
ENV BUILD_DEPS ${PHPIZE_DEPS} \  
pkgconfig \  
libtool  
  
# PHP  
ENV PHP_EXTENSIONS bcmath intl zip mysqli pdo_mysql exif gettext pcntl opcache
gmp bz2 gd  
ENV PHP_EXTENSION_DEPS ${BUILD_DEPS} \  
bzip2-dev \  
gettext-dev \  
libmcrypt-dev \  
gmp-dev@community \  
pkgconfig \  
icu-dev \  
libxml2-dev \  
zlib-dev \  
libressl-dev@edge \  
pcre-dev  
ENV MEDIA_RUNTIME_DEPS \  
imagemagick \  
libpng \  
libjpeg-turbo \  
libwebp \  
libxpm \  
freetype@edge \  
fontconfig \  
ghostscript \  
ffmpeg \  
pngcrush \  
jpegoptim \  
poppler-utils@edge \  
html2text@edge  
ENV MEDIA_BUILD_DEPS \  
imagemagick-dev \  
libpng-dev \  
fontconfig-dev \  
ghostscript-dev \  
pcre-dev \  
libjpeg-turbo-dev \  
libwebp-dev \  
libxpm-dev \  
freetype-dev@edge \  
file  
  
## Alpine iconv support (requires gnu-libiconv@testing)  
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php  
  
COPY php-fpm/php-fpm.conf $PHP_INI_DIR/php-fpm.conf  
  
## Install extensions  
RUN set -xe \  
&& docker-php-source extract \  
&& apk add --no-cache $MEDIA_RUNTIME_DEPS \  
&& apk add --no-cache --virtual .extension-deps $PHP_EXTENSION_DEPS \  
&& apk add --no-cache --virtual .media-build-deps $MEDIA_BUILD_DEPS \  
&& pecl install apcu-5.1.11 redis-3.1.6 imagick-3.4.3 \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-xpm-dir=/usr/include \  
\--with-webp-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& docker-php-ext-enable redis apcu imagick \  
&& docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" $PHP_EXTENSIONS \  
&& apk del .media-build-deps \  
&& apk del .extension-deps \  
&& docker-php-source delete  
## Install composer  
ENV COMPOSER_ALLOW_SUPERUSER=1  
ENV COMPOSER_CACHE_DIR=/mnt/shared/system/composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& mkdir -m 700 -p /mnt/shared/system/composer \  
&& composer global require hirak/prestissimo  
  
# Install S6 Service Manager & Overlay  
RUN set -xe \  
&& curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.16.0/confd-0.16.0-linux-
amd64 -o /usr/local/bin/confd \  
# Install S6 Service Manager  
&& curl -L https://github.com/just-
containers/s6-overlay/releases/download/v1.21.4.0/s6-overlay-amd64.tar.gz -o
/tmp/s6-overlay-amd64.tar.gz \  
&& tar xzf /tmp/s6-overlay-amd64.tar.gz -C / \  
&& rm /tmp/s6-overlay-amd64.tar.gz \  
# Configure application dependencies  
&& mkdir -p /tmp/nginx \  
&& chown nginx /tmp/nginx \  
&& chmod +x /usr/local/bin/confd \  
&& mkdir /etc/confd  
  
COPY s6/etc /etc  
  
# App configuration  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY php/php.ini.tmpl /etc/confd/templates/  
COPY php/php.ini.toml /etc/confd/conf.d/  
RUN set -xe \  
&& confd -onetime -backend env \  
&& chmod -R ugo+X /var/log/nginx/ \  
&& mkdir -m 700 -p \  
/mnt/tmpfs/opcache/file_cache \  
/mnt/tmpfs/opcache/lockfiles \  
/mnt/shared/tmp \  
/srv/app \  
&& chown -R www-data:www-data \  
/mnt/tmpfs \  
/mnt/shared \  
/srv/app  
  
WORKDIR /srv/app  
EXPOSE 80  
EXPOSE 9000  
CMD "/init"  

