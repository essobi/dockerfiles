FROM php:7.1  
RUN apt-get update && apt-get install -y \  
nodejs \  
git \  
wget \  
libmemcached-dev \  
zlib1g-dev \  
libicu-dev \  
zlib1g-dev \  
firebird-dev \  
unzip \  
mysql-client \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
&& pecl install memcached-3.0.3 \  
&& pecl install xdebug-2.5.0 \  
&& curl -Ss --location --output /usr/local/bin/phpunit
https://phar.phpunit.de/phpunit.phar \  
&& chmod +x /usr/local/bin/phpunit \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt pdo_mysql intl interbase zip
soap \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-enable memcached xdebug \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

