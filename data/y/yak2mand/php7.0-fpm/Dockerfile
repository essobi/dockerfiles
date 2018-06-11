FROM php:7.0-fpm  
  
RUN apt-get update -q  
  
RUN apt-get install -y libicu52 libicu-dev libssl-dev pkg-config libcurl3
libcurl4-openssl-dev libmcrypt-dev zlib1g-dev \  
&& docker-php-ext-install -j$(nproc) \  
opcache \  
mbstring \  
bcmath \  
exif \  
iconv \  
mcrypt \  
intl \  
zip \  
curl  
  
RUN php -r "readfile('https://getcomposer.org/installer');" | php --
--install-dir=/usr/local/bin --filename=composer \  
&& chmod +x /usr/local/bin/composer  
  
RUN apt-get install -y libssl-dev  
  
RUN apt-get remove -y --auto-remove libfreetype6-dev libjpeg62-turbo-dev
libpng12-dev libicu-dev libcurl4-openssl-dev libssl-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN usermod -u 1000 www-data  
  

