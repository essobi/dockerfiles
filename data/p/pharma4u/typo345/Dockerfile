FROM php:5.6-apache  
MAINTAINER Nils Hitze <hitze@pharma4u.de>  
  
# Install TYPO3  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends \  
wget \  
# Configure PHP  
libxml2-dev libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
# Install required 3rd party tools  
graphicsmagick && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) mysqli soap gd zip opcache && \  
echo 'always_populate_raw_post_data = -1\nmax_execution_time =
240\nmax_input_vars = 1500\nupload_max_filesize = 32M\npost_max_size = 32M' >
/usr/local/etc/php/conf.d/typo3.ini && \  
# Configure Apache as needed  
a2enmod rewrite && \  
apt-get clean && \  
apt-get -y purge \  
libxml2-dev libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev && \  
pecl install apcu-4.0.11 && \  
echo 'extension=apcu.so' > /usr/local/etc/php/conf.d/apcu.ini && \  
echo '<?php phpinfo();' > /var/www/html/index.php && \  
rm -rf /var/lib/apt/lists/* /usr/src/*  
  
RUN cd /var/www/html && \  
chown -R www-data. .  
  
# Configure volumes  
  
VOLUME /var/www/html/

