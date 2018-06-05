FROM registry.dryusdan.fr/dryusdan/php:7.1  
  
ARG CACHET_VER=2.3.13  
ENV UID=991 GID=991  
  
  
RUN export BUILD_DEPS="build-base \  
wget \  
gnupg \  
autoconf \  
libressl-dev \  
g++ \  
pcre-dev \  
curl-dev \  
libedit-dev \  
gcc \  
zlib-dev \  
make \  
pkgconf \  
wget \  
ca-certificates \  
libxml2-dev" \  
&& apk -U add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS \  
&& apk -U add ${BUILD_DEPS} \  
&& pecl install apcu \  
&& docker-php-ext-enable apcu \  
&& apk del .phpize-deps-configure ${BUILD_DEPS} \  
&& apk -U add git curl mariadb-client \  
&& git clone --branch v${CACHET_VER} https://github.com/CachetHQ/Cachet.git
/cachetHQ  
COPY rootfs /  
WORKDIR cachetHQ  
RUN chmod +x /usr/local/bin/startup \  
&& mv env .env \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer install --no-dev \  
&& apk del git curl \  
&& rm -rf /var/cache/apk/* /tmp/* /root/.gnupg /root/.cache/ /cachetHQ/.git  

