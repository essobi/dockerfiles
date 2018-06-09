FROM alpine  
  
Maintainer Wanjo Chan ( http://github.com/wanjochan/ )  
  
#COPY repositories /etc/apk/  
RUN echo "http://nl.alpinelinux.org/alpine/latest-stable/main/" >
/etc/apk/repositories  
RUN echo "http://nl.alpinelinux.org/alpine/edge/community/" >>
/etc/apk/repositories  
RUN echo "http://nl.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories  
  
RUN apk update && apk upgrade  
  
#RUN apk --update add  
RUN apk add \  
php7-curl \  
php7-gmp \  
php7-json \  
php7-mbstring \  
php7-opcache \  
php7-mysqlnd \  
php7-pdo \  
php7-pdo_mysql \  
php7-session \  
php7-zlib \  
php7-dom \  
php7-xml \  
php7-fpm \  
php7  
  
RUN apk add libwebp libwebp-tools  
  
#RUN apk add php7-gd  
RUN apk add nginx  
  
RUN apk add wget curl bash openssl  
  
#Save Space but will fail the 'apk search'...  
#RUN rm -rf /var/cache/apk/*  

