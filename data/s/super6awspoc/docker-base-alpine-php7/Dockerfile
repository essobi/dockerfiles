FROM alpine:3.5  
MAINTAINER infinityworks  
  
# Install libs and apps  
# Install GCC, g++, etc. to install the PHP7 Redis client  
# from source (see below).  
RUN apk add --no-cache \  
bind-tools \  
curl \  
gettext \  
make \  
netcat-openbsd \  
nginx \  
nodejs \  
tcpdump \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
pkgconf \  
re2c \  
sassc && \  
  
apk add \--no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/main
\  
icu-libs \  
libressl && \  
  
apk add \--no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/community \  
php7 \  
php7-common \  
php7-ctype \  
php7-curl \  
php7-dev \  
php7-dom \  
php7-fpm \  
php7-gettext \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mysqlnd \  
php7-opcache \  
php7-openssl \  
php7-pcntl \  
php7-phar \  
php7-pdo \  
php7-pdo_mysql \  
php7-session \  
php7-simplexml \  
php7-tokenizer \  
php7-xml && \  
  
ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm && \  
  
# Fetch, compile and install the previous version of the PHP Redis client from
source as the latest version is broken.  
curl -L https://github.com/phpredis/phpredis/archive/3.0.0.tar.gz -o
/tmp/3.0.0.tar.gz && \  
tar -xzvf /tmp/3.0.0.tar.gz -C /tmp && \  
cd /tmp/phpredis-3.0.0 && \  
phpize7 && \  
./configure && \  
make && \  
make install && \  
echo "extension=redis.so" > /etc/php7/conf.d/01_redis.ini && \  
  
# Install composer from script instead of via apk to avoid pulling in  
# unwanted php5 packages.  
cd /tmp && curl -sS https://getcomposer.org/installer | php && mv
composer.phar /usr/local/bin/composer  
  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 -o /usr/local/bin/confd  
  
# Install S6 Service Manager  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
# Set up users  
RUN adduser -DH fpm && \  
adduser -DH node  
  
# Configure application dependencies  
RUN mkdir -p /tmp/nginx && \  
chown nginx /tmp/nginx && \  
chmod +x /usr/local/bin/confd && \  
mkdir /etc/confd  
  
# Web stuff  
COPY s6/etc /etc  
  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY php-fpm/php-fpm.conf /etc/php7/php-fpm.conf  
COPY php/php.ini.tmpl /etc/confd/templates/  
COPY php/php.ini.toml /etc/confd/conf.d/  
  
RUN chmod -R ugo+X /var/log/nginx/  
COPY php-fpm-exporter /php-fpm-exporter  
  
WORKDIR /  
  
# php.ini flags  
ENV RUNMODE_PRODUCTION=1  
# S6 flags  
# (0) - ignore errors  
# (1) - proceed with a WARN if error is found  
# (2) - crash S6 if an error is found  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2  
EXPOSE 80  
EXPOSE 6755  

