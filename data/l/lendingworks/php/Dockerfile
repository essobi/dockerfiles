# One of 'cli' or 'fpm' (as per https://hub.docker.com/_/php/).  
ARG PHP_TYPE  
ARG PHP_VERSION=7.2  
ARG ALPINE_VERSION=3.7  
FROM php:${PHP_VERSION}-${PHP_TYPE}-alpine${ALPINE_VERSION}  
  
# Increment this to trigger a full rebuild.  
ENV CONTAINER_VERSION '1.0.0'  
  
RUN apk add --no-cache --update --virtual build-deps \  
autoconf \  
g++ \  
make \  
zlib-dev \  
freetype \  
libjpeg-turbo \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
libxml2-dev \  
libssh2-dev \  
curl-dev \  
postgresql-dev \  
libmemcached-dev \  
cyrus-sasl-dev \  
&& apk add --no-cache \  
libpng \  
libmemcached \  
bash \  
sed \  
mysql-client \  
postgresql-client \  
curl \  
wget \  
&& docker-php-ext-install -j$(nproc) \  
mbstring \  
zip \  
bcmath \  
gd \  
curl \  
json \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
opcache \  
soap \  
xml \  
&& pecl install igbinary memcached redis ssh2-1.1.2 \  
&& docker-php-ext-enable igbinary memcached redis ssh2 \  
&& rm -rf /tmp/pear \  
&& apk del --no-cache build-deps  
  
COPY ./conf/fpm-zz-docker.conf /usr/local/etc/php-fpm.d/zz-docker.conf  
EXPOSE 9090  
  
COPY ./conf/php.ini /usr/local/etc/php/  
  
RUN mkdir -p /data/www  
WORKDIR /data/www  

