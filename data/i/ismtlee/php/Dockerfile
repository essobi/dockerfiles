FROM php:7-fpm-alpine  
  
RUN apk add --no-cache --update \  
autoconf file g++ gcc binutils isl libatomic libc-dev musl-dev make re2c
libstdc++ libgcc binutils-libs mpc1 mpfr3 gmp libgomp postgresql-dev \  
coreutils \  
freetype-dev \  
libjpeg-turbo-dev \  
libltdl \  
libmcrypt-dev \  
libpng-dev \  
pcre-dev \  
imap-dev \  
openssl-dev \  
postgresql-dev \  
&& docker-php-ext-install iconv mcrypt mysqli pdo pdo_mysql pdo_pgsql zip
bcmath \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure imap --with-imap --with-imap-ssl \  
&& docker-php-ext-install imap \  
&& pecl install igbinary \  
&& pecl install redis \  
&& pecl install mongodb \  
&& pecl install yaf \  
&& docker-php-ext-enable igbinary redis yaf mongodb \  
&& apk del autoconf file g++ gcc binutils isl libatomic libc-dev musl-dev make
re2c libstdc++ libgcc binutils-libs mpc1 mpfr3 gmp libgomp \  
&& rm -rf /var/cache/apk/*  
  
#COPY ./php.ini /usr/local/etc/php/php.ini  

