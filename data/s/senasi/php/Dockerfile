FROM php:7.0-fpm-alpine  
  
WORKDIR /build  
  
RUN mkdir /build/libiconv  
  
COPY libiconv.patch /build/libiconv/  
  
RUN apk add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS && \  
cd /build/libiconv && \  
curl -SL http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.14.tar.gz | tar -xz
--strip-components=1 && \  
patch -p1 -i libiconv.patch && \  
./configure --prefix=/usr/local && \  
make && \  
make install && \  
rm -rf /build && \  
apk add --no-cache --virtual .run-deps \  
libsodium \  
icu-libs \  
openssl \  
libmcrypt \  
zlib \  
libxslt \  
libxml2 \  
freetype \  
libwebp \  
libjpeg \  
libpng \  
c-client && \  
apk add --no-cache --virtual .build-deps \  
bash \  
libsodium-dev \  
icu-dev \  
openssl-dev \  
libmcrypt-dev \  
zlib-dev \  
libxslt-dev \  
libxml2-dev \  
freetype-dev \  
libwebp-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
imap-dev && \  
docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ --with-freetype-
dir=/usr/include/ --with-webp-dir=/usr/include/ && \  
docker-php-ext-configure imap --with-imap-ssl=/usr && \  
pecl install mongodb mailparse libsodium && \  
docker-php-ext-enable mongodb mailparse sodium && \  
docker-php-ext-install calendar gd pcntl pdo_mysql soap sockets xsl zip
opcache mcrypt bcmath intl imap mysqli && \  
apk del .build-deps  
  
RUN set -ex \  
&& cd /usr/local/etc \  
&& { \  
echo '[www]'; \  
echo 'pm.max_children = 10'; \  
echo 'pm.max_requests = 500'; \  
} | tee php-fpm.d/zzz-docker.conf \  
&& { \  
echo '[php]'; \  
echo 'memory_limit = 512M'; \  
echo 'post_max_size = 256M'; \  
echo 'upload_max_size = 128M'; \  
} | tee php/php.ini  
  
ENV LD_PRELOAD /usr/local/lib/preloadable_libiconv.so  
  

