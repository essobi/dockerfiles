FROM php:7-fpm-alpine  
  
ENV LIBICONV_VERSION 1.14  
  
RUN apk upgrade --update && apk add grep build-base tar \  
autoconf file g++ gcc binutils isl libatomic libc-dev musl-dev make re2c
libstdc++ libgcc binutils-libs mpc1 mpfr3 gmp libgomp icu-dev \  
coreutils \  
freetype-dev \  
libjpeg-turbo-dev \  
libltdl \  
libmcrypt-dev \  
libpng-dev \  
&& curl -SL
http://ftp.gnu.org/pub/gnu/libiconv/libiconv-${LIBICONV_VERSION}.tar.gz | tar
-xz -C ~/ \  
&& mv ~/libiconv-${LIBICONV_VERSION} ~/libiconv \  
&& rm /usr/bin/iconv \  
&& sed -i 's!_GL_WARN_ON_USE (gets, "gets is a security hole - use fgets
instead");!/* _GL_WARN_ON_USE (gets, "gets is a security hole - use fgets
instead"); */!' ~/libiconv/srclib/stdio.in.h \  
&& ~/libiconv/configure \  
&& make && make install \  
&& docker-php-ext-install iconv mcrypt mysqli mysqlnd pdo pdo_mysql zip intl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& apk del grep build-base tar \  
autoconf file g++ gcc binutils isl libatomic libc-dev musl-dev make re2c
libstdc++ libgcc binutils-libs mpc1 mpfr3 gmp libgomp \  
&& rm -rf /var/cache/apk/* ~/libiconv  
  
ENV LD_PRELOAD /usr/local/lib/preloadable_libiconv.so  

