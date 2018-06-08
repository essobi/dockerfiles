FROM php:5.6.36-fpm-alpine3.7  
RUN apk update && apk add zlib-dev  
  
RUN docker-php-ext-install iconv \  
pcntl \  
zip \  
iconv \  
pdo_mysql \  
exif \  
opcache  
  
RUN apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev
libjpeg-turbo-dev && \  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
docker-php-ext-install -j${NPROC} gd && \  
apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev zlib-dev  
  
ADD php.ini /usr/local/etc/php/php.ini  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer \  
&& chmod +x /usr/bin/composer  
  
RUN composer global require hirak/prestissimo  
  
WORKDIR /app  

