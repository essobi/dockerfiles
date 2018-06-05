FROM php:7.2-fpm-alpine  
LABEL maintainer="Johannes Tegnér <johannes@jitesoft.com>"  
  
ENV PACKAGES="autoconf binutils gcc make isl libatomic musl-dev re2c libstdc++
libgcc binutils-libs mpc1 mpfr3 gmp libgomp coreutils redis freetype-dev
libjpeg-turbo-dev libltdl libmcrypt-dev libpng-dev" \  
INSTALL_EXTENSIONS="iconv mysqli pdo pdo_mysql zip gd"  
RUN apk add --no-cache $PACKAGES \  
&& pecl install redis-3.1.4 \  
&& docker-php-ext-enable redis \  
&& docker-php-ext-install $INSTALL_EXTENSIONS \  
&& php -v  
  
WORKDIR /app  

