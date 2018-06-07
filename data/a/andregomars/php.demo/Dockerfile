FROM php:7.1.11-fpm-alpine  
MAINTAINER Andre Shen  
  
RUN apk add \--no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev
libjpeg-turbo-dev && \  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/  
  
RUN docker-php-ext-install -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null ||
1) \  
mysqli  
  
RUN apk del --no-cache freetype-dev libpng-dev libjpeg-turbo-dev  
  
# RUN docker-php-ext-install mysqli iconv gd mbstring fileinfo curl xmlreader
xmlwriter spl ftp mysqli  
# VOLUME /var/www/html  
RUN chown -R www-data:www-data /var/www/html  
# RUN chmod -R g+w .  

