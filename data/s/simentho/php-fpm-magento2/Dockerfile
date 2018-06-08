FROM php:7.0-fpm-alpine  
# php:7.0-alpine source code:  
# https://github.com/docker-
library/php/tree/ddc7084c8a78ea12f0cfdceff7d03c5a530b787e/7.0/fpm/alpine  
# See "Best practices for writing Dockerfiles":  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices  
# Commands for adding PHP extensions are adapted from StackOverflow answer:  
# see http://stackoverflow.com/a/39218681  
##  
# This environment variable is used by "docker-php-ext-install"  
# See https://github.com/docker-
library/php/blob/ddc7084c8a78ea12f0cfdceff7d03c5a530b787e/7.0/alpine/docker-
php-ext-install#L88  
##  
ENV PHPIZE_DEPS \  
autoconf \  
cmake \  
file \  
freetype-dev \  
g++ \  
git \  
gcc \  
icu-dev \  
libc-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libxslt-dev \  
make \  
pcre-dev \  
pkgconf \  
re2c  
  
RUN set -x && \  
apk update && apk add \  
freetype \  
icu \  
libjpeg-turbo \  
libmcrypt \  
libpng \  
libxslt \  
openssh \  
openssl \  
tini && \  
docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
NPROC=$(getconf _NPROCESSORS_ONLN || 1) && \  
docker-php-ext-install -j${NPROC} \  
gd \  
intl \  
mcrypt \  
mysqli \  
pdo_mysql \  
xsl \  
zip && \  
rm /var/cache/apk/*  
  
# Install Magerun2  
ENV N98_MAGERUN2_CHECkSUM
'd94f4b938f9c43d4a42f0e0ddcd38a051525f1ab0eb0cd84816ca48bbe5d2c20
n98-magerun2.phar'  
RUN wget https://files.magerun.net/n98-magerun2.phar -O
/root/n98-magerun2.phar && \  
cd /root && \  
echo "${N98_MAGERUN2_CHECkSUM}" | sha256sum -c - && \  
chmod +x n98-magerun2.phar && \  
mv n98-magerun2.phar /usr/local/bin/ && \  
cd -  
  
COPY config/php.ini /usr/local/etc/php/  
COPY config/magento.conf /usr/local/etc/php-fpm.d/zzz-magento.conf  
  
VOLUME ["/var/www"]

