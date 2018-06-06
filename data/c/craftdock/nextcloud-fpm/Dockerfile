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
&& apk-install \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ \  
wget \  
# Create php repository folder  
&& mkdir -p /php.earth/x86_64/ \  
&& cd /php.earth/x86_64/ \  
# Copy all packages from php.earth repo to /php.earth/x86_64  
&& wget -r -nd -np -k http://repos.php.earth/alpine/v3.7/x86_64/ \  
# Clear apk's cache  
&& apk-cleanup  
  
  
# Nextcloud  
FROM craftdock/alpine-php7:7.1  
  
LABEL maintainer="Hexosse <hexosse@gmail.com>" \  
description="Nextcloud image based on alpine with runit process supervisor."  
# Nextcloud version  
ENV NEXTCLOUD_VERSION 13.0.2  
  
# Trust this project public key to trust the php packages.  
ADD https://repos.php.earth/alpine/phpearth.rsa.pub
/etc/apk/keys/phpearth.rsa.pub  
# Copy all packages from  
COPY \--from=php_repository /php.earth/x86_64 /tmp/php.earth/x86_64  
# Ensure nextcloud user exists  
RUN set -x \  
&& addgroup -S nextcloud \  
&& adduser -S -D -G nextcloud nextcloud \  
&& adduser nextcloud www-data  
  
RUN \  
# Print executed commands  
set -x \  
# Update repository indexes  
&& apk-update \  
# Add recommanded packages :
https://docs.nextcloud.com/server/12/admin_manual/installation/source_installation.html#prerequisites-
label  
&& apk-install \--repository /tmp/php.earth \  
# Required : ctype, dom, GD, iconv, JSON, libxml, mbstring, posix, SimpleXML,
XMLReader, XMLWriter ,zip, zlib  
php7.1-ctype \  
php7.1-dom \  
php7.1-gd \  
php7.1-iconv \  
php7.1-json \  
libxml2 \  
php7.1-mbstring \  
php7.1-posix \  
php7.1-simplexml \  
php7.1-xmlreader \  
php7.1-xmlwriter \  
php7.1-zip \  
php7.1-zlib \  
# Database connectors : pdo_sqlite, pdo_mysql, pdo_pgsql  
php7.1-pdo_sqlite \  
php7.1-pdo_mysql \  
php7.1-pgsql \  
# Recommended packages : curl, fileinfo, bz2, intl, mcrypt, openssl  
php7.1-curl \  
php7.1-fileinfo \  
php7.1-bz2 \  
php7.1-intl \  
php7.1-mcrypt \  
php7.1-openssl \  
# Required for specific apps : ldap, **smbclient**, ftp, imap  
php7.1-ldap \  
php7.1-ftp \  
php7.1-imap \  
# Recommended for specific apps : exif, gmp  
php7.1-exif \  
php7.1-gmp \  
# For enhanced server performance : apcu, memcached, redis  
php7.1-apcu \  
php7.1-memcached \  
php7.1-redis \  
# For preview generation : imagick, avconv or ffmpeg, OpenOffice or
LibreOffice  
imagemagick-libs \  
php7.1-imagick \  
ffmpeg libva \  
libreoffice icu-libs \  
# For command line processing : pcntl  
php7.1-pcntl \  
# Other tools  
icu-libs \  
boost-filesystem \  
# Add packages used in this image  
&& apk-install \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ \  
rsync \  
# Download, build and instal libsmbclient-php  
# Add necessary packages to install libsmbclient-php  
&& apk-install \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ \  
samba \  
# Add temporary packages to compile libsmbclient-php  
&& apk-install \--repository /tmp/php.earth \--repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ \--virtual .build-dependencies \  
git \  
autoconf \  
automake \  
file \  
g++ \  
gcc \  
make \  
php7.1-dev \  
re2c \  
samba-dev \  
zlib-dev \  
# Compile libsmbclient-php  
&& git clone https://github.com/eduardok/libsmbclient-php.git /tmp/smbclient \  
&& cd /tmp/smbclient \  
&& phpize \  
&& ./configure \--with-php-config=/usr/bin/php-config \  
&& make \  
&& make install \  
# Activate libsmbclient-php  
&& echo "extension=\"smbclient.so\"" > /etc/php7/conf.d/00_smbclient.ini \  
# Clear apk's cache  
&& rm -rf /etc/service.d/php-fpm \  
&& apk-remove .build-dependencies \  
&& apk-cleanup  
  
  
# Download, install and verify Nextcloud  
RUN curl -fsSL -o nextcloud.tar.bz2 \  
"https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2"
\  
&& mkdir /usr/src/ \  
&& tar -xjf nextcloud.tar.bz2 -C /usr/src/ \  
&& rm nextcloud.tar.bz2 \  
#  
&& rm -rf /usr/src/nextcloud/updater \  
&& mkdir -p /usr/src/nextcloud/assets \  
&& mkdir -p /usr/src/nextcloud/config \  
&& mkdir -p /usr/src/nextcloud/custom_apps \  
&& mkdir -p /usr/src/nextcloud/themes \  
&& mkdir -p /usr/src/nextcloud/updater \  
&& chmod +x /usr/src/nextcloud/occ  
# Copy scripts  
COPY /rootfs /  
  
# Add volume to allow persistence  
VOLUME ["/nextcloud", "/var/www"]  

