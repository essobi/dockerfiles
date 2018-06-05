FROM php:7-alpine  
  
RUN apk add --no-cache libmcrypt-dev libltdl icu-dev zlib-dev git mysql-client
\  
&& docker-php-ext-install mbstring mcrypt intl pdo_mysql mysqli zip \  
&& echo -e "[Date]\ndate.timezone = Asia/Tokyo" >> /usr/local/etc/php/php.ini
\  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
CMD [ "docker-php-entrypoint php -a" ]  

