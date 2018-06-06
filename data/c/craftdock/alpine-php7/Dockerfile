# Php repository.  
# (This is a workaround when behind a proxy to prevent 'Permission denied'
from php.earth repo)  
FROM craftdock/alpine-base as php_repository  
  
RUN \  
# Print executed commands  
set -x \  
# Update repository indexes  
&& apk-update \  
# Add packages  
&& apk-install --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ \  
wget \  
# Create php repository folder  
&& mkdir -p /php.earth/x86_64/ \  
&& cd /php.earth/x86_64/ \  
# Copy all packages from php.earth repo to /php.earth/x86_64  
&& wget -r -nd -np -k http://repos.php.earth/alpine/v3.7/x86_64/ \  
# Clear apk's cache  
&& apk-cleanup  
  
  
# Php  
FROM craftdock/alpine-runit:latest  
  
LABEL maintainer="Hexosse <hexosse@gmail.com>" \  
description="Minimal Alpine image with php7 and runit process supervisor."  
  
ENV PHP_VERSION=7.2  
# Trust this project public key to trust the php packages.  
ADD https://repos.php.earth/alpine/phpearth.rsa.pub
/etc/apk/keys/phpearth.rsa.pub  
  
# Copy all packages from  
COPY --from=php_repository /php.earth/x86_64 /tmp/php.earth/x86_64  
  
RUN \  
# Print executed commands  
set -x \  
# Update repository indexes  
&& apk-update \  
# Add packages  
&& apk-install --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ \  
ca-certificates \  
libcap \  
memcached \  
openssh-client \  
tar \  
zip \  
wget \  
# https://github.com/docker-library/php/issues/494  
libressl \  
# Add php packages & composer  
&& apk-install --repository /tmp/php.earth \  
php7.2 \  
php7.2-fpm \  
# php libs  
php7.2-apcu \  
php7.2-bcmath \  
php7.2-common \  
php7.2-ctype \  
php7.2-curl \  
php7.2-dom \  
php7.2-fileinfo \  
php7.2-gd \  
php7.2-iconv \  
php7.2-json \  
php7.2-mbstring \  
php7.2-memcached \  
php7.2-mysqli \  
php7.2-opcache \  
php7.2-openssl \  
php7.2-pdo \  
php7.2-pdo_mysql \  
php7.2-pgsql \  
php7.2-pdo_sqlite \  
php7.2-phar \  
php7.2-redis \  
php7.2-session \  
php7.2-simplexml \  
php7.2-sqlite3 \  
php7.2-tokenizer \  
php7.2-xml \  
php7.2-xmlreader \  
php7.2-xmlwriter \  
php7.2-zip \  
php7.2-zlib \  
# Composer  
composer \  
php7.2-composer \  
# symblink php7 to php  
&& ln -s "/etc/php/$PHP_VERSION/" /etc/php7 \  
# Create default webroot folder  
&& mkdir -p /var/www \  
&& chown www-data:www-data /var/www \  
# Clear apk's cache  
&& apk-cleanup  
  
# Copy scripts  
COPY /rootfs /  
# Expose php-fpm port  
EXPOSE 9000  

