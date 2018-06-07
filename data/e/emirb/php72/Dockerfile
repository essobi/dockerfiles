# PHP 7.2 image with php cli, fpm, memcache, maxmind, mongo and blackfire
extensions  
FROM phusion/baseimage:latest  
  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ARG DEBIAN_FRONTEND=noninteractive  
ARG LC_ALL=C.UTF-8  
  
# Install essential packages  
RUN set -e; \  
add-apt-repository -y ppa:ondrej/php && \  
add-apt-repository ppa:maxmind/ppa && \  
curl https://packagecloud.io/gpg.key | apt-key add - && \  
echo "deb http://packages.blackfire.io/debian any main" | tee
/etc/apt/sources.list.d/blackfire.list && \  
apt-get update && apt-get install -y --no-install-recommends \  
curl \  
git \  
locales \  
ca-certificates \  
curl \  
zip \  
memcached \  
php-pear \  
# install libmaxminddb  
libmaxminddb0 libmaxminddb-dev mmdb-bin \  
# install PHP  
php-memcache \  
php-memcached \  
php-redis \  
php7.2 \  
php7.2-common php7.2-json php7.2-opcache php7.2-readline \  
php7.2-cli \  
php7.2-curl \  
php7.2-dev \  
php7.2-fpm \  
php7.2-gd \  
php7.2-gmp \  
php7.2-intl \  
php7.2-json \  
php7.2-mbstring \  
php7.2-oauth \  
php7.2-opcache \  
php7.2-soap \  
php7.2-xml \  
php7.2-zip \  
php7.2-yaml \  
nginx \  
blackfire-agent blackfire-php \  
# mongodb extension requirement  
pkg-config libssl-dev \  
jq && \  
# Install MongoDB  
pecl channel-update pecl.php.net && pecl install
channel://pecl.php.net/geospatial-0.2.0 && pecl install mongodb-1.4.2 && echo
"extension=mongodb.so" > /etc/php/7.2/mods-available/mongodb.ini && \  
pecl install xdebug-2.6.0 && \  
phpenmod -v 7.2 mongodb zip memcache xdebug && \  
# Install Maxmind  
mkdir -p /usr/local/share/maxmind && \  
curl -s -L -C -
"http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz" -o
/usr/local/share/maxmind/GeoLite2-City.mmdb.gz && \  
gunzip /usr/local/share/maxmind/GeoLite2-City.mmdb.gz && \  
useradd nginx && mkdir -p /var/lib/php/session && chgrp nginx
/var/lib/php/session && \  
# xdebug log dir  
test ! -e /var/log/xdebug && mkdir /var/log/xdebug && chown nginx:nginx
/var/log/xdebug && \  
curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin && \  
composer global require hirak/prestissimo && \  
# Set locales  
locale-gen en_US && \  
# Set up CA root certificates  
mkdir -p /etc/ssl/certs/ && update-ca-certificates --fresh && \  
# Clean  
apt-get purge -y --auto-remove && apt-get clean all && rm -rf /var/lib/apt/ &&
/etc/init.d/memcached start && php -v  
  
CMD /sbin/my_init  

