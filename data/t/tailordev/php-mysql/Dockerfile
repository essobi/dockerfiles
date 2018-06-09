FROM php:7.1-alpine  
MAINTAINER TailorDev <hello@tailordev.fr>  
  
RUN apk upgrade \--update && apk add \  
mysql-client \  
imap-dev \  
openssl-dev \  
&& docker-php-source extract \  
&& docker-php-ext-install pdo pdo_mysql \  
&& docker-php-ext-configure imap --with-imap --with-imap-ssl \  
&& docker-php-ext-install imap \  
&& docker-php-source delete \  
&& rm -rf /var/cache/apk/*  

