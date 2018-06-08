# https://www.revive-adserver.com/  
FROM alpine:3.3  
MAINTAINER Alexei Smirnov  
  
WORKDIR /var/www/html  
  
RUN apk update  
RUN apk add -U gzip \  
nginx \  
php-curl \  
php-fpm \  
php-gd \  
php-json \  
php-mysql \  
php-opcache \  
php-openssl \  
php-pgsql \  
php-phar \  
php-xml \  
php-zlib \  
tar  
  
RUN wget -O- https://download.revive-adserver.com/revive-adserver-4.0.1.tar.gz
| tar xz --strip 1  
  
RUN chown -R nobody:nobody . \  
&& rm -rf /var/cache/apk/*  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80  
CMD php-fpm && nginx -g 'daemon off;'  

