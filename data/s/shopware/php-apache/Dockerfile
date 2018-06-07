FROM php:7.1-apache  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
libpng12-dev \  
libfreetype6-dev \  
libjpeg-dev \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN docker-php-ext-configure gd --with-jpeg-dir=/usr/lib --with-freetype-
dir=/usr/include \  
&& docker-php-ext-install pdo pdo_mysql mbstring gd  
  
RUN a2enmod rewrite  
  
COPY shopware.ini /usr/local/etc/php/conf.d/shopware.ini  
  
CMD ["apache2-foreground"]  

