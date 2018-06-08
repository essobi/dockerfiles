FROM php:7.1.10-apache  
  
#
-----------------------------------------------------------------------------  
# SERVICES & PHP EXTENSIONS  
#
-----------------------------------------------------------------------------  
RUN \  
apt-get update && \  
apt-get install -y \  
zlib1g-dev \  
libicu-dev \  
g++ \  
vim \  
libmcrypt-dev \  
php-pear \  
curl \  
wget \  
git \  
zip \  
cron \  
sendmail-bin \  
libxml2-dev \  
npm \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN a2enmod rewrite  
  
COPY grav-skeleton-grayscale-site-v1.0.0 /var/www/html  
  
RUN chmod -R 777 /var/www/html/cache/  
RUN chmod -R 777 /var/www/html/logs/  
RUN chmod -R 777 /var/www/html/images/  
RUN chmod -R 777 /var/www/html/assets/  
RUN chmod -R 777 /var/www/html/user/  
RUN chmod -R 777 /var/www/html/backup/  

