FROM php:7.0-apache  
  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
zip unzip dialog locales \  
git-core \  
g++ \  
zlib1g-dev \  
libicu-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) zip pdo pdo_mysql intl gd bcmath \  
&& rm -rf /var/lib/apt/lists/* \  
&& a2enmod rewrite \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
COPY apache2.conf /etc/apache2/  

