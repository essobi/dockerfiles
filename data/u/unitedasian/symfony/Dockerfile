FROM unitedasian/php-fpm  
  
MAINTAINER Olivier Pichon <op@united-asian.com>  
  
RUN apk update && apk add --update \  
php-ctype \  
php-dom \  
php-iconv \  
php-intl \  
php-json \  
php-pdo_mysql \  
php-xml \  
&& rm -rf /var/cache/apk/*  
  
COPY entrypoint.d /entrypoint.d  
  
ONBUILD COPY . /var/www  

