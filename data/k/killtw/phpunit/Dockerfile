FROM php:7.2-alpine  
  
RUN apk add --no-cache --virtual build-dependencies g++ make autoconf libpng
libjpeg-turbo && \  
apk add -U libpng-dev libjpeg-turbo-dev && \  
pecl install xdebug && \  
docker-php-ext-enable xdebug && \  
docker-php-ext-configure gd --with-png-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd exif pcntl && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
composer global require hirak/prestissimo && \  
wget -O phpunit https://phar.phpunit.de/phpunit-7.phar && \  
chmod +x phpunit && \  
mv phpunit /usr/local/bin && \  
apk del build-dependencies && \  
rm -rf /tmp/* /src /var/cache/apk/*  

