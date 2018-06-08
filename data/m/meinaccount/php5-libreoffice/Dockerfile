FROM php:5-fpm  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
libreoffice \  
&& rm -rf /var/lib/apt/lists/*  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr  
RUN docker-php-ext-install \  
gd \  
mbstring \  
pdo \  
pdo_mysql \  
mysqli \  
zip  
  
WORKDIR /var/www  
COPY php.ini /usr/local/etc/php/  

