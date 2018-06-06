ARG PHP_VERSION=7.2  
ARG ALPINE_VERSION=3.7  
FROM php:${PHP_VERSION}-fpm-alpine${ALPINE_VERSION}  
  
ENV LANG="en_US.UTF-8" \  
LC_ALL="en_US.UTF-8" \  
LANGUAGE="en_US.UTF-8" \  
TERM="xterm" \  
DEBIAN_FRONTEND="noninteractive" \  
COMPOSER_ALLOW_SUPERUSER=1  
RUN apk add --no-cache git  
  
COPY \--from=composer:latest /usr/bin/composer /usr/bin/composer  
COPY php/php.ini /usr/local/etc/php/php.ini  
  
WORKDIR /var/www/html  
  
# Prevent Symfony Flex from generating a project ID at build time  
ARG SYMFONY_SKIP_REGISTRATION=1  
RUN apk add --update && \  
apk add --no-cache --virtual .build-deps \  
vim \  
curl \  
bash \  
git \  
supervisor \  
tzdata \  
wget \  
libxml2 \  
zlib \  
libpng \  
freetype \  
libjpeg-turbo \  
libmcrypt \  
unzip && \  
apk del .build-deps  
  
RUN buildDeps=" build-base re2c file readline-dev autoconf binutils bison \  
libxml2-dev curl-dev freetype-dev openssl-dev \  
libjpeg-turbo-dev libpng-dev libwebp-dev libmcrypt-dev \  
gmp-dev icu-dev libmemcached-dev linux-headers" \  
&& apk --update add $buildDeps  
  
# composer install  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install php extensions  
RUN docker-php-ext-install -j$(nproc) iconv mbstring pdo_mysql xml zip && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
  
COPY /php/docker-entrypoint.sh /usr/local/bin/docker-entrypoint  
RUN chmod +x /usr/local/bin/docker-entrypoint  
  
# Install phpunit  
RUN wget -O phpunit https://phar.phpunit.de/phpunit-7.phar \  
&& chmod +x phpunit \  
&& mv phpunit /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint"]  
CMD ["php-fpm"]  
  
EXPOSE 9000  

