FROM attractgrouphub/alpine-php7-nginx-composer:2.0  
MAINTAINER Amondar  
  
RUN apk --update add supervisor nodejs nodejs-npm bash git openssl-dev g++
autoconf make  
RUN npm install --global yarn && \  
composer global require "hirak/prestissimo:^0.3"  
  
# Install mongo  
RUN pecl install mongodb  
RUN echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/mongodb.ini  
RUN apk del --no-cache autoconf g++ make

