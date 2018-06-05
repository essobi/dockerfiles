FROM php:7.0-apache  
  
RUN echo "[PHP]\nmemory_limit = 256M" > /usr/local/etc/php/php.ini  
  
WORKDIR /var/www/html/  
  
RUN apt-get update && yes | apt-get install wget libpng12-dev libjpeg62-turbo-
dev  
  
RUN wget http://files.ubergallery.net/releases/UberGallery-v2.4.8.tar.gz \  
&& tar -zxf UberGallery-v2.4.8.tar.gz \  
&& mv UberGallery-v2.4.8/* . \  
&& cp resources/sample.galleryConfig.ini resources/galleryConfig.ini \  
&& chmod 777 resources/cache \  
&& docker-php-ext-install -j$(nproc) gd  
  
VOLUME /var/www/html/gallery-images  

