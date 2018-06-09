FROM alpine:latest  
  
RUN apk add \--update --no-cache wget curl git \  
php7 \  
php7-mysqli php7-pdo php7-pdo_mysql \  
php7-redis \  
php7-sockets php7-json php7-bcmath \  
php7-phar php7-curl php7-openssl php7-mbstring php7-iconv php7-tokenizer
php7-dom php7-xmlwriter php7-xml  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer

