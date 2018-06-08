ARG PHP_VERSION=7  
ARG ALPINE_VERSION=3.7  
  
FROM php:$PHP_VERSION-fpm-alpine$ALPINE_VERSION  
MAINTAINER zier <florianzier@users.noreply.github.com>  
  
  
# use proxy arguments for a working connection while building  
# ARGs for HTTP_PROXY, HTTPS_PROXY, FTP_PROXY, NO_PROXY are available by
default  
ARG HTTP_PROXY_REQUEST_FULLURI="false"  
ARG HTTPS_PROXY_REQUEST_FULLURI="false"  
COPY [ "conf/certs", "/etc/ssl/certs/" ]  
  
  
# copy php.ini, append timezone afterwards  
COPY [ "conf/php.ini", "/usr/local/etc/php/" ]  
# set correct timezone for alpine and in php.ini  
ARG TZ="UTC"  
ARG INTL="en"  
RUN apk add --update --no-cache tzdata \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& echo $TZ > /etc/timezone \  
&& (echo "[DATE]" & echo "date.timezone=\"${TZ}\";" & echo "") >>
/usr/local/etc/php/php.ini \  
&& (echo "[intl]" & echo "intl.default_locale=\"${INTL}\";" \  
& echo "intl.use_exceptions=1;" & echo "intl.error_level=E_WARNING;") >>
/usr/local/etc/php/php.ini  
#&& apk del tzdata # delete other timezones  
  
  
# install common php extensions  
RUN apk add --no-cache libzip-dev bzip2-dev icu-dev ssmtp \  
&& docker-php-ext-configure mysqli --with-mysqli=mysqlnd \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql \  
&& docker-php-ext-configure zip --with-libzip=/usr/lib \  
&& docker-php-ext-configure intl --enable-intl \  
&& docker-php-ext-install mysqli pdo_mysql zip bz2 intl  
  
# install gnu iconv, supports options //IGNORE and //TRANSLIT  
RUN apk add --no-cache --allow-untrusted --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing gnu-libiconv  
ENV LD_PRELOAD="/usr/lib/preloadable_libiconv.so php"  
  
  
# install composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -sS https://getcomposer.org/installer \  
| php -- --install-dir=/usr/local/bin --filename=composer  
  
  
# install additional modules: Xdebug, OPcache, APCu  
COPY [ "conf/xdebug.ini", "/usr/local/etc/php/conf.d/" ]  
RUN apk add --no-cache --virtual build-dependencies icu-dev g++ make autoconf
\  
&& docker-php-ext-install opcache \  
&& docker-php-source extract \  
&& pecl install xdebug-beta apcu-beta apcu_bc-beta \  
&& docker-php-ext-enable xdebug \  
&& docker-php-ext-enable apcu --ini-name 10-docker-php-ext-apcu.ini \  
&& docker-php-ext-enable apc --ini-name 20-docker-php-ext-apc.ini \  
&& docker-php-source delete \  
&& apk del build-dependencies \  
&& rm -rf /tmp/*  
  
# install LDAP  
#RUN apk add --no-cache openldap-dev \  
# && docker-php-ext-configure ldap --with-libdir=lib/ \  
# && docker-php-ext-install ldap  

