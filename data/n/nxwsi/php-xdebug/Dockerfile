FROM php:7.1  
RUN apt-get update && apt-get install -y \  
unzip \  
git \  
libcurl3-dev \  
zlib1g-dev \  
libxml2-dev  
  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
RUN docker-php-ext-install pdo pdo_mysql mbstring curl zip dom iconv  
  
# Install GD  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  

