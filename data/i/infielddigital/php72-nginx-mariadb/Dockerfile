FROM php:7.2-fpm  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev  
  
RUN docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
RUN pecl install mcrypt-1.0.1  
RUN docker-php-ext-enable mcrypt  
  
RUN docker-php-ext-install mysqli  
  
CMD ["php-fpm"]  

