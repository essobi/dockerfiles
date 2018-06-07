FROM richarvey/nginx-php-fpm:latest  
  
MAINTAINER Heiko Holland  
  
LABEL Name=nginx-php-fpm-with-imap  
LABEL Version=0.0.1  
  
# install some packages and imap  
RUN apk upgrade --update \  
&& apk add autoconf file g++ gcc binutils isl libatomic libc-dev musl-dev make
re2c libstdc++ libgcc binutils-libs mpc1 mpfr3 gmp libgomp \  
imap-dev \  
busybox-suid \  
&& docker-php-ext-configure imap --with-imap --with-imap-ssl \  
&& docker-php-ext-install imap  
  
# remove not needed files  
RUN apk del autoconf file g++ gcc binutils isl libatomic libc-dev musl-dev
make re2c libstdc++ libgcc binutils-libs mpc1 mpfr3 gmp libgomp \  
&& rm -rf /var/cache/apk/*  
  
RUN supervisorctl restart php-fpm  

