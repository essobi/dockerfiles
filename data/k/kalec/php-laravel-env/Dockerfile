FROM php:7.1.10-alpine  
MAINTAINER Giuseppe Trombino <g.trombino@gmail.com>  
LABEL maintainer="Giuseppe Trombino <g.trombino@gmail.com>" \  
php="7.1.10"  
  
RUN BUILD_DEPENDENCIES="build-base \  
autoconf" \  
DEV_DEPENDENCIES="libtool \  
curl-dev \  
icu-dev \  
libmcrypt-dev \  
libvpx-dev \  
jpeg-dev \  
libpng-dev \  
libxpm-dev \  
zlib-dev \  
freetype-dev \  
libxml2-dev \  
expat-dev \  
bzip2-dev \  
gmp-dev \  
imap-dev \  
openldap-dev \  
unixodbc-dev \  
postgresql-dev \  
sqlite-dev \  
aspell-dev \  
net-snmp-dev \  
tidyhtml-dev@community \  
pcre-dev" \  
&& echo '@community http://dl-cdn.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories \  
&& apk update && apk upgrade -U -a && apk add \  
openssh-client \  
nodejs-current@community \  
nodejs-current-npm@community \  
git \  
$BUILD_DEPENDENCIES \  
$DEV_DEPENDENCIES \  
&& docker-php-ext-install mbstring mcrypt pdo_mysql pdo_pgsql curl json intl
gd xml zip bz2 opcache bcmath \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& apk del --purge $BUILD_DEPENDENCIES \  
&& php -v \  
&& git --version \  
&& cd ~ \  
&& curl -O
https://raw.githubusercontent.com/laravel/laravel/master/composer.json \  
&& EXPECTED_SIGNATURE=$(curl -q -sS https://composer.github.io/installer.sig)
\  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', 'composer-
setup.php');") \  
&& if [ "$EXPECTED_SIGNATURE" != "$ACTUAL_SIGNATURE" ]; then >&2 echo 'ERROR:
Invalid installer signature' && rm composer-setup.php && exit 1; fi \  
&& php composer-setup.php --quiet --install-dir=/usr/local/bin
--filename=composer \  
&& RESULT=$? \  
&& rm composer-setup.php \  
&& composer --version \  
&& composer install --no-autoloader --no-scripts --no-suggest \  
&& exit $RESULT  

