FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y \  
# For GD  
libpng-dev \  
libjpeg-dev \  
# For pgsql  
libpq-dev \  
libbz2-dev \  
# For intl  
libicu-dev \  
# For mcrypt  
libmcrypt-dev \  
# For smbclient  
libsmbclient-dev \  
  
&& rm -rf /var/lib/apt/lists/* \  
  
  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-configure pgsql --with-pgsql=/usr/local/pgsql \  
  
  
&& docker-php-ext-install \  
gd \  
zip \  
pdo \  
pdo_pgsql \  
pgsql \  
bz2 \  
intl \  
mcrypt \  
opcache \  
  
  
&& pecl install APCu \  
&& pecl install redis \  
&& pecl install smbclient \  
  
  
&& docker-php-ext-enable \  
apcu \  
redis \  
smbclient \  
  
&& usermod -u 988 www-data \  
&& groupmod -g 988 www-data  

