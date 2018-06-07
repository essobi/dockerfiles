FROM composer:latest as composer  
  
# ---  
  
FROM php:fpm-alpine  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
COMPOSER_ALLOW_SUPERUSER=1 \  
S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \  
S6_KEEP_ENV=1 \  
S6_READ_ONLY_ROOT=1  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS \  
${PHPIZE_DEPS} \  
&& apk add --no-cache --no-progress \  
ca-certificates \  
git \  
openssh-client \  
shadow \  
\  
# Install melody  
\  
&& curl --location --output /usr/bin/melody
"http://get.sensiolabs.org/melody.phar" \  
&& chmod +x /usr/bin/melody \  
\  
# Install php-ext-amqp  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS_PHP_AMQP \  
rabbitmq-c-dev \  
&& apk add --no-cache --no-progress \  
rabbitmq-c \  
&& pecl install amqp \  
&& docker-php-ext-enable amqp \  
\  
# Install php-ext-apcu  
\  
&& pecl install apcu \  
&& docker-php-ext-enable apcu \  
\  
# Install php-ext-bcmath  
\  
&& docker-php-ext-install bcmath \  
\  
# Install php-ext-blackfire  
\  
&& export PHP_VERSION="$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;")"
\  
&& curl --location --user-agent Docker
"https://blackfire.io/api/v1/releases/probe/php/alpine/amd64/${PHP_VERSION}" |
tar --directory /tmp --extract --gzip \  
&& mv /tmp/blackfire-*.so "$(php -r "echo
ini_get('extension_dir');")/blackfire.so" \  
&& docker-php-ext-enable blackfire \  
\  
# Install php-ext-gd  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS_PHP_GD \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
&& apk add --no-cache --no-progress \  
freetype \  
libjpeg-turbo \  
libpng \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
\  
# Install php-ext-gmp  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS_PHP_GMP \  
gmp-dev \  
&& apk add --no-cache --no-progress \  
gmp \  
&& docker-php-ext-install gmp \  
\  
# Install php-ext-gnupg  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS_PHP_GNUPG \  
gpgme-dev \  
&& apk add --no-cache --no-progress \  
gpgme \  
&& pecl install gnupg \  
&& docker-php-ext-enable gnupg \  
\  
# Install php-ext-igbinary  
\  
&& pecl install igbinary \  
&& docker-php-ext-enable igbinary \  
\  
# Install php-ext-intl  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS_PHP_INTL \  
icu-dev \  
&& apk add --no-cache --no-progress \  
icu \  
&& docker-php-ext-install intl \  
\  
# Install php-ext-mysql  
\  
&& docker-php-ext-install pdo_mysql \  
\  
# Install php-ext-opcache  
\  
&& docker-php-ext-install opcache \  
\  
# Install php-ext-pgsql  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS_PHP_PGSQL \  
postgresql-dev \  
&& apk add --no-cache --no-progress \  
postgresql-libs \  
&& docker-php-ext-install pdo_pgsql pgsql \  
\  
# Install php-ext-redis  
\  
&& pecl install redis \  
&& docker-php-ext-enable redis \  
\  
# Install php-ext-xdebug  
\  
&& pecl install xdebug \  
\  
# Install php-ext-xml  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS_PHP_XML \  
libxml2-dev \  
&& apk add --no-cache --no-progress \  
libxml2 \  
&& docker-php-ext-install xml \  
\  
# Install php-ext-zip  
\  
&& docker-php-ext-install zip \  
\  
# Install php-cs-fixer  
\  
&& curl --location --output /usr/bin/php-cs-fixer
"http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar" \  
&& chmod +x /usr/bin/php-cs-fixer \  
\  
# Install timonier/dumb-entrypoint  
\  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/s6-overlay/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
\  
# Clean  
\  
&& apk del --no-progress \  
BUILD_DEPS \  
BUILD_DEPS_PHP_AMQP \  
BUILD_DEPS_PHP_GD \  
BUILD_DEPS_PHP_GMP \  
BUILD_DEPS_PHP_GNUPG \  
BUILD_DEPS_PHP_INTL \  
BUILD_DEPS_PHP_PGSQL \  
BUILD_DEPS_PHP_XML \  
&& rm -f -r \  
/tmp/* \  
/usr/local/etc/php-fpm.d/*  
  
COPY --from=composer /usr/bin/composer /usr/bin/composer  
  
COPY ./rootfs /  
  
ENTRYPOINT [ "/init" ]  

