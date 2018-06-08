FROM php:7.1-apache  
  
RUN a2enmod rewrite  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libssl-dev \  
libicu-dev \  
libtidy-dev \  
libpq-dev \  
libmcrypt-dev \  
git \  
&& docker-php-ext-install -j$(nproc) \  
iconv \  
mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) \  
gd \  
pdo pdo_mysql \  
tidy \  
mbstring \  
bcmath \  
json \  
mysqli \  
zip \  
intl \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

