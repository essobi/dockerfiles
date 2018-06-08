# Alpine Ticks:  
# - http://blog.zot24.com/tips-tricks-with-alpine-docker/  
# - http://www.sandtable.com/reduce-docker-image-sizes-using-alpine/  
  
# Based on Alpine 3.6  
ARG PHP_VERSION=7.2.3  
FROM php:${PHP_VERSION}-fpm-alpine  
  
########################################################################################################################  
# INIT
#################################################################################################################  
  
LABEL maintainer="Xplouder <jfasxx@hotmail.com>"  
  
RUN apk update && apk upgrade  
  
########################################################################################################################  
# PHP EXTENSIONS
#######################################################################################################  
# ref: https://hub.docker.com/r/sinso/phpfpm-typo3/~/dockerfile/  
  
  
# Imagick extension  
# ref: https://github.com/docker-library/php/issues/105  
RUN set -ex \  
&& apk add --no-cache imagemagick \  
&& apk add --no-cache --virtual imagick-deps $PHPIZE_DEPS imagemagick-dev
libtool \  
&& export CFLAGS="$PHP_CFLAGS" CPPFLAGS="$PHP_CPPFLAGS" LDFLAGS="$PHP_LDFLAGS"
\  
&& pecl install imagick-3.4.3 \  
&& docker-php-ext-enable imagick \  
&& apk del imagick-deps  
  
# Intl extension  
RUN set -ex \  
# Necessary lib to load Intl extension  
&& apk add --no-cache icu-libs \  
&& apk add --no-cache --virtual intl-deps icu-dev \  
&& docker-php-ext-install intl \  
&& apk del --purge intl-deps  
  
  
# Xdebug extension  
# ref: https://hub.docker.com/r/zaherg/php-7.1-xdebug-alpine/~/dockerfile/  
RUN set -ex \  
&& apk add --no-cache --virtual xdebug-deps autoconf freetype-dev g++ make
gettext-dev \  
&& docker-php-source extract \  
&& pecl install xdebug-2.6.0 \  
&& docker-php-ext-enable xdebug \  
&& docker-php-source delete \  
&& apk del --purge xdebug-deps  
  
  
## YAML extension  
ENV PHPIZE_DEPS autoconf dpkg-dev dpkg file g++ gcc libc-dev make pcre-dev
pkgconf re2c  
ENV PHP_INI_DIR /usr/local/etc/php  
  
RUN set -xe \  
&& apk add --no-cache --virtual yaml-deps $PHPIZE_DEPS \  
&& apk add --no-cache yaml-dev \  
&& pecl install yaml-2.0.2 \  
&& echo "extension=yaml.so" >> $PHP_INI_DIR/conf.d/01_yaml.ini \  
&& apk del --purge yaml-deps  
  
  
# Other extensions  
RUN set -ex \  
# Necessary libs  
&& apk add --no-cache libmcrypt \  
&& apk add --no-cache --virtual other-deps libmcrypt-dev libxml2-dev libpng-
dev libjpeg-turbo-dev \  
&& docker-php-ext-install pdo_mysql soap zip mbstring iconv mysqli exif bcmath
opcache pdo gd \  
&& apk del --purge other-deps  
  
#
######################################################################################################################  
# # CLI TOOLS
##########################################################################################################  
RUN apk add --no-cache vim nano git tree wget bash curl  
  
#
######################################################################################################################  
# # EXTRA LIBS
#########################################################################################################  
  
RUN apk add --no-cache openssh-client libmcrypt net-tools mysql-client  
  
# Replace nodejs by nodejs-current when using a image based on Alpine 3.6  
RUN apk add --no-cache nodejs \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#
######################################################################################################################  
# # PHALCON
############################################################################################################  
ARG PHALCON_VERSION=3.3.2  
  
# https://hub.docker.com/r/npulidom/alpine-phalcon/~/dockerfile/  
# Compile Phalcon  
RUN set -xe \  
&& apk add --no-cache --virtual phalcon-deps libtool re2c pcre-dev file
autoconf gcc make g++ \  
&& set -xe \  
&& curl -LO
https://github.com/phalcon/cphalcon/archive/v${PHALCON_VERSION}.tar.gz \  
&& tar xzf v${PHALCON_VERSION}.tar.gz \  
&& cd cphalcon-${PHALCON_VERSION}/build \  
&& sh ./install \  
&& docker-php-ext-enable phalcon \  
&& cd ../.. \  
&& rm -rf v${PHALCON_VERSION}.tar.gz cphalcon-${PHALCON_VERSION} \  
# Install Phalcon Devtools, see https://github.com/phalcon/phalcon-devtools/  
#&& curl -LO https://github.com/phalcon/phalcon-
devtools/archive/v${PHALCON_VERSION}.tar.gz \  
#&& tar xzf v${PHALCON_VERSION}.tar.gz \  
#&& mv phalcon-devtools-${PHALCON_VERSION} /usr/local/phalcon-devtools \  
#&& ln -s /usr/local/phalcon-devtools/phalcon.php /usr/local/bin/phalcon \  
#&& rm -rf v${PHALCON_VERSION}.tar.gz \  
&& apk del --purge phalcon-deps  
  
#
######################################################################################################################  
# # Tweaks
#############################################################################################################  
  
WORKDIR /code  
  
# Workaround for Linux develop environments -----------------------  
ARG GROUP_USER_ID=0  
ARG USER_ID=0  
ARG USER_NAME=root  
# Only run if the provided USER_ID arg is different of 0 (root)  
RUN if [ "${USER_ID}" != "0" ]; then \  
set -xe \  
&& addgroup -g ${GROUP_USER_ID} -S ${USER_NAME} \  
&& adduser -u ${USER_ID} -D -S -G ${USER_NAME} ${USER_NAME} \  
&& mkdir -p /home/${USER_NAME} \  
&& chmod -R 777 /home/${USER_NAME} \  
&& chown -R ${USER_ID}:${GROUP_USER_ID} /home/${USER_NAME} \  
; fi  
# -----------------------------------------------------------------  
  
RUN rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf tmp/*  

