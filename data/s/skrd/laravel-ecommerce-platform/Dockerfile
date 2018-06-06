FROM php:7.1-fpm-alpine  
  
RUN apk add --no-cache \  
icu-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
postgresql-dev && \  
docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ && \  
docker-php-ext-install gd intl pdo_pgsql zip  
  
RUN echo "memory_limit = 512M" >> $PHP_INI_DIR/php.ini && \  
echo "post_max_size = 32M" >> $PHP_INI_DIR/php.ini && \  
echo "upload_max_filesize = 32M" >> $PHP_INI_DIR/php.ini && \  
sed -i 's/listen = 127.0.0.1:9000/listen = 9000/' /usr/local/etc/php-
fpm.d/www.conf  

