FROM php:7.2-cli-alpine  
  
MAINTAINER Mikael Kermorgant <mikael@kgtech.fi>  
  
  
# Install dependencies  
RUN apk --no-cache --update add \  
libsasl \  
db \  
curl \  
&& apk add --no-cache --virtual .php-deps \  
git \  
make \  
freetype \  
icu \  
libpng \  
libjpeg-turbo \  
libxml2 \  
postgresql-libs \  
sqlite-libs \  
zlib \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
freetype-dev \  
g++ \  
icu-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
libxml2-dev \  
postgresql-dev \  
sqlite-dev \  
zlib-dev \  
&& pecl install xdebug-2.6.0 \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install \  
bcmath \  
intl \  
gd \  
opcache \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
zip \  
&& docker-php-ext-enable \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
intl \  
xdebug \  
&& apk del .build-deps \  
&& rm -rf /tmp/* /usr/local/lib/php/doc/* /var/cache/apk/* \  
&& { find /usr/local/lib -type f -print0 | xargs -0r strip --strip-all -p
2>/dev/null || true; } \  
&& mkdir /var/www  
  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
COPY --from=composer:1.6 /usr/bin/composer /usr/bin/composer  
  
WORKDIR /var/www  
COPY ["entrypoint.sh", "/"]  
ENTRYPOINT ["/entrypoint.sh"]  

