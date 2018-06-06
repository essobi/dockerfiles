FROM php:7.1-alpine  
  
MAINTAINER Dmitry Boyko <dmitry@thebodva.com>  
  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
  
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');"  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer && \  
rm -rf /tmp/composer-setup.php  
  
RUN php -r "copy('https://phar.phpunit.de/phpunit.phar','/tmp/phpunit.phar');"  
RUN chmod +x /tmp/phpunit.phar  
RUN mv /tmp/phpunit.phar /usr/local/bin/phpunit  
  
RUN apk add --no-cache git unzip openssh  
  
RUN apk add --no-cache \  
freetype-dev \  
libjpeg-turbo-dev \  
libxml2-dev \  
autoconf \  
g++ \  
gcc \  
libtool \  
make \  
libmcrypt-dev \  
libpng-dev \  
sqlite-dev \  
curl-dev \  
pcre-dev \  
&& docker-php-ext-install -j11 iconv mcrypt pdo_mysql pcntl pdo_sqlite zip
curl bcmath mbstring mysqli opcache soap\  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j1 gd \  
&& docker-php-ext-enable iconv mcrypt gd pdo_mysql pcntl pdo_sqlite zip curl
bcmath mbstring mysqli soap\  
&& rm -rf /tmp/* /var/cache/apk/*  
  
RUN set -ex \  
&& apk add --no-cache --virtual .phpize-deps $PHPIZE_DEPS imagemagick-dev
libtool \  
&& export CFLAGS="$PHP_CFLAGS" CPPFLAGS="$PHP_CPPFLAGS" LDFLAGS="$PHP_LDFLAGS"
\  
&& pecl install imagick mongodb \  
&& docker-php-ext-enable imagick mongodb \  
&& apk add --no-cache --virtual .imagick-runtime-deps imagemagick \  
&& apk del .phpize-deps  
  
RUN docker-php-ext-install exif \  
&& docker-php-ext-enable exif  

