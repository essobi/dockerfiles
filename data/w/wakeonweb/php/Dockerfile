FROM php:7.2-fpm-alpine  
  
# Install deps  
RUN apk add --no-cache $PHPIZE_DEPS c-client curl git mysql-client nodejs-
current-npm openssh-client python \  
cyrus-sasl-dev icu-dev icu-libs imap imap-dev libmcrypt libmcrypt-dev
libmemcached libmemcached-dev \  
libxml2 libxml2-dev postgresql-dev postgresql-libs sqlite-dev sqlite-libs zlib
zlib-dev \  
&& pecl install memcached redis xdebug \  
&& docker-php-ext-enable memcached redis xdebug \  
&& docker-php-ext-install bcmath imap intl mbstring opcache pcntl pdo
pdo_mysql pdo_pgsql soap zip \  
&& npm i -g dredd \  
&& apk info | grep "\\-dev" | xargs apk del autoconf dpkg file g++ gcc pkgconf
re2c python \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Config  
COPY xdebug.ini .  
  
RUN cat xdebug.ini >> /usr/local/etc/php/docker-php-ext-xdebug.ini \  
&& sed -i -e 's/^user = www-data/user = dockeruser/' -e 's/^group = www-
data/group = dockergroup/' /usr/local/etc/php-fpm.d/www.conf  

