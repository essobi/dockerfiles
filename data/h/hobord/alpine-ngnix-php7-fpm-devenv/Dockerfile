FROM alpine:latest  
MAINTAINER Balazs Szabo <balazs.szabo@gmail.com>  
  
ENV PHPREDIS_VERSION php7  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk update \  
&& apk add bash nginx ca-certificates \  
&& apk --update add shadow \  
php7 \  
php7-dom \  
php7-ctype \  
php7-curl \  
php7-fpm \  
php7-gd \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqlnd \  
php7-opcache \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_sqlite \  
php7-exif \  
php7-posix \  
php7-session \  
php7-xml \  
php7-iconv \  
php7-phar \  
php7-openssl \  
php7-zip \  
php7-soap \  
php7-zlib \  
php7-ftp \  
php7-bz2 \  
&& rm -rf /var/cache/apk/*  
  
# fix php-fpm "Error relocating /usr/bin/php-fpm: __flt_rounds: symbol not
found" bug  
RUN apk add -u musl  
RUN rm -rf /var/cache/apk/*  
  
ADD files/nginx.conf /etc/nginx/  
ADD files/php-fpm.conf /etc/php7/  
ADD files/run.sh /  
RUN chmod +x /run.sh  
  
RUN usermod -u 1000 nginx  
RUN apk del shadow  
  
EXPOSE 80  
VOLUME ["/DATA","/DATA/htdocs"]  
  
CMD ["/run.sh"]  

