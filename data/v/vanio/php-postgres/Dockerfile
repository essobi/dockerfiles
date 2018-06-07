FROM php:7.2-apache  
  
RUN apt-get update && apt-get install -y \  
git \  
zlib1g-dev \  
libicu-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpq-dev \  
gnupg && \  
curl -O
http://security.debian.org/pool/updates/main/libp/libpng/libpng12-0_1.2.50-2+deb8u2_amd64.deb
&& \  
dpkg -i libpng12-0_1.2.50-2+deb8u2_amd64.deb && \  
apt-get install -f && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install zip intl gd pgsql pdo_pgsql opcache && \  
pecl install apcu-5.1.8 && \  
docker-php-ext-enable apcu && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
a2enmod rewrite && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
curl -sS https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs  
  
  
COPY php.ini /usr/local/etc/php/  

