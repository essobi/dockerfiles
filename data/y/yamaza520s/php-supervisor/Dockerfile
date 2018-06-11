FROM php:7.0.7-fpm-alpine  
  
MAINTAINER Ats Ymzk  
  
COPY ./etc/php/php.ini /usr/local/etc/php/  
COPY ./etc/php/php-fpm.conf /usr/local/etc/php-fpm.d/www.conf  
# RUN cat /usr/local/etc/php-fpm.conf  
# apk update  
RUN apk update && apk upgrade  
  
# timezone  
RUN apk add tzdata \  
&& cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& echo "Asia/Tokyo" > /etc/timezone  
  
# supervisor  
RUN apk add python py-pip \  
&& pip install supervisor  
  
# install PHP dev dependencies  
RUN buildDeps="build-base re2c file readline-dev autoconf binutils bison \  
libxml2-dev curl-dev freetype-dev openssl-dev \  
libjpeg-turbo-dev libpng-dev libwebp-dev libmcrypt-dev \  
gmp-dev icu-dev" \  
&& apk --update add $buildDeps  
  
RUN docker-php-ext-install iconv mcrypt pdo_mysql mysqli mbstring  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Packagistのミラーサイトを設定  
# Composerの通信を並列化するプラグインのインストール  
RUN composer global config repositories.packagist composer
https://packagist.jp \  
&& composer global require hirak/prestissimo  
  
# remove PHP dev dependencies  
RUN apk del $buildDeps  
  
# other clean up  
RUN cd / \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/* \  
&& ln -sf /dev/stderr /var/log/php-fpm.log \  
&& mkdir -p /var/www/html  

