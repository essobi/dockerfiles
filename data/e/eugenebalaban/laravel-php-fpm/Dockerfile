FROM php:7.1-fpm-alpine  
  
RUN set -xe \  
&& apk add --no-cache \  
libmcrypt-dev \  
libxml2-dev \  
libintl \  
gettext-dev \  
openldap-dev \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
icu-dev \  
  
# Install composer and prestissimo  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer global require "hirak/prestissimo:^0.3" \  
  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
  
# Install PHP modules  
&& docker-php-ext-install bcmath \  
calendar fileinfo iconv json mbstring \  
gettext mcrypt pcntl pdo pdo_mysql soap \  
tokenizer zip ldap gd intl \  
&& rm -rf /var/cache/apk/*  
  
COPY . /var/www/html

