FROM php:7.0-apache  
  
LABEL maintainer="zerozwy@gmail.com"  
  
RUN apt update && apt install -y libjpeg-dev libpng12-dev libfreetype6-dev
libmagickwand-dev Imagemagick unzip wget \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd && pecl install imagick && docker-php-ext-enable
imagick  
RUN wget https://github.com/Studio-42/elFinder/archive/2.1.29.zip && unzip
2.1.29.zip && rm -f 2.1.29.zip && mv elFinder-2.1.29/* ./ && rm -rf
elFinder-2.1.29  
RUN chown -R www-data:www-data * && mv php/connector.minimal.php-dist
php/connector.minimal.php  
RUN echo "DirectoryIndex elfinder.html" >> .htaccess  
  
VOLUME [ "/var/www/html/files" ]  

