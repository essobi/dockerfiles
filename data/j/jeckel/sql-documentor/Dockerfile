FROM php:alpine  
MAINTAINER Julien MERCIER <devci@j3ck3l.me>  
# This Dockerfile build a php image with composer included  
# It used for this tutorials.  
#  
# Reminder : It's not recommanded to have composer installed in container for
production  
# as this is required for developpement only.  
RUN wget
https://raw.githubusercontent.com/composer/getcomposer.org/863c57de1807c99d984f7b56f0ea56ebd7e5045b/web/installer
-O - -q | php -- --quiet &&\  
mv composer.phar /usr/local/bin/composer && \  
composer self-update  
  
#RUN apk --update upgrade \  
# && apk add autoconf gcc g++ yaml-dev re2c make  
RUN apk add --no-cache --virtual .build-deps \  
g++ make autoconf yaml-dev  
  
# Define composer cache directory  
RUN mkdir -p /tmp/composer && chmod 777 /tmp/composer  
ENV COMPOSER_CACHE_DIR=/tmp/composer  
  
RUN docker-php-ext-install pdo_mysql  
  
#RUN pecl install yaml \  
# && docker-php-ext-enable yaml  
RUN pecl channel-update pecl.php.net  
RUN pecl install yaml-2.0.0 && docker-php-ext-enable yaml  
  
COPY . /sql-documentor  
  
WORKDIR /sql-documentor  
  
RUN composer install  
CMD php generate.php  

