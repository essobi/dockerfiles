FROM alpine:latest  
  
Maintainer Alexey Popov <leemo-studio.net>  
  
RUN apk add --update --no-cache \  
curl \  
php7 \  
php7-bz2 \  
php7-dom \  
php7-fileinfo \  
php7-imagick \  
php7-json \  
php7-mcrypt \  
php7-mbstring \  
php7-opcache \  
php7-openssl \  
php7-pdo \  
php7-pdo_mysql \  
php7-phar \  
php7-session \  
php7-soap \  
php7-tokenizer \  
php7-xml \  
php7-zip \  
php7-zlib \  
&& rm -rf /var/cache/apk/* \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
EXPOSE 9000  
CMD ["php-fpm7"]  

