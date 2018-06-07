FROM php:7.2.2-fpm-alpine3.7  
LABEL maintainer="https://github.com/halcyon-suite/halcyon" \  
description="Another web interface of Mastodon"  
  
ENV NODE_ENV=production \  
COMPOSER_ALLOW_SUPERUSER=true  
  
EXPOSE 2800  
WORKDIR /halcyon  
  
RUN apk -U upgrade \  
&& apk add \  
curl \  
git \  
nginx \  
nodejs \  
nodejs-npm \  
yarn \  
build-base \  
libmemcached-dev \  
libmcrypt-dev \  
libxml2-dev \  
zlib-dev \  
autoconf \  
cyrus-sasl-dev \  
libgsasl-dev \  
postgresql-dev \  
supervisor \  
&& docker-php-ext-install \  
pdo \  
pdo_pgsql \  
mbstring \  
tokenizer \  
xml \  
&& pecl channel-update pecl.php.net \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached \  
&& mkdir -p /var/log/nginx /var/log/supervisor \  
&& rm -rf /var/cache/apk/*  
  
COPY ./composer.phar /usr/local/bin/composer  
COPY ./installation/php.ini /usr/local/etc/php/php.ini  
COPY ./installation/nginx.conf /etc/nginx/nginx.conf  
COPY ./installation/zzz-www.conf /usr/local/etc/php-fpm.d  
COPY ./installation/supervisord.conf /etc/supervisord.conf  
COPY . /halcyon  
  
RUN mkdir -p /halcyon/storage /halcyon/bootstrap/cache \  
&& chmod -R 777 /halcyon/storage /halcyon/bootstrap/cache \  
&& chmod +x /usr/local/bin/composer; sync \  
&& yarn cache clean  
  
VOLUME ["/halcyon"]  
  
CMD ["supervisord"]  

