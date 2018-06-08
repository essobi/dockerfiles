FROM php:fpm-alpine  
RUN apk update && apk add \--no-cache coreutils freetype-dev libjpeg-turbo-dev
libltdl libmcrypt-dev libpng-dev icu-dev libxml2-dev openssl-dev libxslt-dev \  
&& apk add \--no-cache autoconf m4 perl file g++ gcc binutils isl libatomic
libc-dev musl-dev make re2c libmagic binutils-libs mpc1 mpfr3 gmp libgomp \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mbstring intl mysqli
pdo_mysql zip sockets soap simplexml xsl opcache \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && docker-php-ext-install -j$(nproc) gd \  
&& pecl install mongodb && docker-php-ext-enable mongodb \  
&& apk del \--purge autoconf m4 perl file g++ gcc binutils isl libatomic libc-
dev musl-dev make re2c libmagic binutils-libs mpc1 mpfr3 gmp libgomp \  
&& /usr/bin/curl -sS https://getcomposer.org/installer | /usr/local/bin/php
\-- --install-dir=/usr/local/bin --filename=composer  
RUN addgroup -g 1000 projadm && adduser -D -G projadm -u 1000 projadm && sed
-i 's/www-data/projadm/' /usr/local/etc/php-fpm.d/www.conf  

