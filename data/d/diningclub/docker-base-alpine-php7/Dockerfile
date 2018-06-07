FROM alpine:3.7  
LABEL maintainer = "infinityworks"  
  
# Install libs and apps  
RUN apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing gnu-libiconv  
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php  
  
RUN apk update && apk add --no-cache --upgrade \  
libbsd \  
bind-tools \  
ca-certificates \  
curl \  
gettext \  
make \  
netcat-openbsd \  
nginx \  
nodejs \  
tcpdump \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
pkgconf \  
re2c \  
logrotate \  
apk-tools \  
sassc && \  
update-ca-certificates 2>/dev/null || true && \  
apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/main \  
icu-libs \  
libressl && \  
apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/community \  
php7 \  
php7-bcmath \  
php7-common \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-fpm \  
php7-gettext \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mysqlnd \  
php7-mysqli \  
php7-opcache \  
php7-openssl \  
php7-pcntl \  
php7-phar \  
php7-pdo \  
php7-pdo_mysql \  
php7-session \  
php7-simplexml \  
php7-tokenizer \  
php7-xml \  
php7-zip \  
php7-dev \  
php7-zlib \  
php7-iconv \  
bzip2-dev \  
php7-gd \  
php7-bz2 \  
php7-fileinfo \  
php7-xmlreader \  
php7-xmlwriter \  
php7-exif \  
php7-pear \  
php7-apcu \  
libwebp && \  
ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm && \  
# Fetch, compile and install the previous version of the PHP Redis client from
source as the latest version is broken.  
curl -L https://github.com/phpredis/phpredis/archive/3.1.6.tar.gz -o
/tmp/3.1.6.tar.gz && \  
tar -xzvf /tmp/3.1.6.tar.gz -C /tmp && \  
cd /tmp/phpredis-3.1.6 && \  
phpize7 && \  
./configure && \  
make -j$(nproc) && \  
make install && \  
echo "extension=redis.so" > /etc/php7/conf.d/01_redis.ini && \  
# Install composer from script instead of via apk to avoid pulling in  
# unwanted php5 packages.  
cd /tmp && curl -sS https://getcomposer.org/installer | php && mv
composer.phar /usr/local/bin/composer && \  
composer global require hirak/prestissimo && \  
apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/main \  
imagemagick imagemagick-dev libpng-dev libpng pngcrush jpegoptim exiftool
poppler-utils html2text libtool git && \  
pecl install imagick && \  
echo "extension=imagick.so" | tee /etc/php7/conf.d/imagick.ini && \  
curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.15.0/confd-0.15.0-linux-
amd64 -o /usr/local/bin/confd && \  
# Install S6 Service Manager  
curl -L https://github.com/just-
containers/s6-overlay/releases/download/v1.21.4.0/s6-overlay-amd64.tar.gz -o
/tmp/s6-overlay-amd64.tar.gz && \  
tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && \  
# Set up users  
adduser -DH fpm && \  
adduser -DH node && \  
# Configure application dependencies  
mkdir -p /tmp/nginx && \  
chown nginx /tmp/nginx && \  
chmod +x /usr/local/bin/confd && \  
mkdir /etc/confd  
  
# Web stuff  
COPY s6/etc /etc  
  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY php-fpm/php-fpm.conf /etc/php7/php-fpm.conf  
COPY php/php.ini.tmpl /etc/confd/templates/  
COPY php/php.ini.toml /etc/confd/conf.d/  
COPY s6/etc/logrotate.conf /etc/logrotate.conf  
COPY s6/etc/logrotate.d/* /etc/logrotate.d/  
  
# php.ini flags  
ENV RUNMODE_PRODUCTION=1  
RUN confd -onetime -backend env  
RUN chmod -R ugo+X /var/log/nginx/  
  
WORKDIR /  
  
RUN mkdir -m 700 -p /tmp/pimcore/log /mnt/shared/cache/ /mnt/shared/system &&
\  
chown -R fpm:fpm /tmp/pimcore /mnt/shared/cache/ /mnt/shared/system  
  
RUN rm /var/cache/apk/*  
  
# S6 flags  
# (0) - ignore errors  
# (1) - proceed with a WARN if error is found  
# (2) - crash S6 if an error is found  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2  
ENV COMPOSER_ALLOW_SUPERUSER=1  
  
EXPOSE 80  
EXPOSE 6755  
  
CMD "/init"  

