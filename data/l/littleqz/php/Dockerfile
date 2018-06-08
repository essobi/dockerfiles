FROM alpine:3.3  
ENV PHP_VERSION 5.5.32  
RUN echo "http://nl.alpinelinux.org/alpine/v3.0/main" > /etc/apk/repositories
&& \  
apk update && \  
apk add php=5.5.32-r0 php-json php-openssl php-phar php-zlib php-dom \  
php-zip php-ctype php-curl php-xml php-gd php-mcrypt && \  
mkdir -p /var/www && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /var/www  

