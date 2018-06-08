FROM php:7.1.17-cli-alpine3.7  
  
RUN apk --no-cache add \  
libpng-dev \  
icu-dev \  
libmcrypt-dev \  
libxml2-dev \  
libxslt-dev \  
jpeg-dev \  
&& docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install \  
bcmath \  
gd \  
intl \  
mcrypt \  
opcache \  
pdo_mysql \  
soap \  
xsl \  
zip  
  
COPY php.ini /usr/local/etc/php/  

