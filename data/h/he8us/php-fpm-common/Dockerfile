FROM php:7.1-fpm-alpine  
  
MAINTAINER Cedric Michaux <cedric@he8us.be>  
  
ENV PHP_PORT 9000  
ENV CONFD_VERSION 0.14.0  
ENV IMAGICK_VERSION 3.4.3  
  
EXPOSE $PHP_PORT  
  
COPY entrypoint.sh /app/entrypoint.sh  
COPY confd/ /etc/confd  
  
  
RUN \  
curl -L -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd  
  
RUN \  
apk --no-cache add \  
freetype-dev \  
icu-dev \  
imagemagick-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libtool \  
pcre-dev \  
wget \  
zip  
  
RUN \  
apk --no-cache add \  
\--virtual .phpize-deps \  
build-base \  
autoconf \  
&& export CFLAGS="$PHP_CFLAGS" CPPFLAGS="$PHP_CPPFLAGS" LDFLAGS="$PHP_LDFLAGS"
\  
&& pecl install imagick-${IMAGICK_VERSION} \  
&& docker-php-ext-enable imagick \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install \  
bcmath \  
gd \  
exif \  
intl \  
mbstring \  
mcrypt \  
pdo_mysql \  
zip \  
&& apk del .phpize-deps  
  
  
ENTRYPOINT ["/app/entrypoint.sh"]  
  
CMD ["php-fpm"]  

