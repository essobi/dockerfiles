FROM php:5.6-apache  
  
RUN apt-get update -y && apt-get install -y \  
libpng12-dev libtidy-dev libjpeg62-turbo-dev libfreetype6-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd mysqli tidy \  
&& a2enmod rewrite  
  
RUN echo '[Custom]\n\  
date.timezone = "Pacific/Auckland"\n\  
memory_limit = 512M\n\  
post_max_size = 128M\n\  
upload_max_filesize = 128M\n'\  
>> /usr/local/etc/php/conf.d/custom.ini  
  
RUN usermod -u 1000 www-data \  
&& usermod -G staff www-data  

