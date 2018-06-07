# OS  
FROM npulidom/alpine-nginx-php:latest  
LABEL maintainer="nicolas.pulido@crazycake.cl"  
# phalcon version  
ENV PHALCON_VERSION=3.3.2  
# iconv  
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so  
# install escentials  
RUN apk add \--update \--no-cache \--repository=http://dl-
cdn.alpinelinux.org/alpine/edge/testing \  
# compiler & tools  
make \  
g++ \  
autoconf \  
file \  
libtool \  
re2c \  
pcre-dev \  
# iconv & gd  
gnu-libiconv \  
php7-iconv@php \  
php7-gd@php \  
php7-redis@php \  
php7-dev@php \  
php7-pear@php \  
&& \  
# symlinks  
ln -s /usr/bin/php-config7 /usr/bin/php-config && \  
ln -s /usr/bin/phpize7 /usr/bin/phpize && \  
# phalcon php  
set -xe && \  
curl -LO
https://github.com/phalcon/cphalcon/archive/v${PHALCON_VERSION}.tar.gz && \  
tar xzf v${PHALCON_VERSION}.tar.gz && \  
# compile  
cd cphalcon-${PHALCON_VERSION}/build && ./install && \  
echo "extension=phalcon.so" | tee -a /etc/php7/conf.d/20_phalcon.ini && \  
cd ../.. && rm -rf v${PHALCON_VERSION}.tar.gz cphalcon-${PHALCON_VERSION} \  
&& \  
# clean dev libs  
apk del \  
make \  
g++ \  
autoconf \  
file \  
libtool \  
re2c \  
pcre-dev \  
php7-dev \  
php7-pear \  
&& rm -rf /var/cache/apk/*  

