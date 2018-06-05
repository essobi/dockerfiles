FROM php:5.6-apache  
  
ADD
https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer
/usr/src/  
RUN a2enmod rewrite \  
&& apt-get update \  
&& apt-get install -y ghostscript pdftohtml imagemagick libmemcached11
libmemcachedutil2 \  
build-essential libmemcached-dev libz-dev openssh-client git-core
libmagickwand-dev html2ps libxml2-utils \--no-install-recommends \  
&& pecl install memcache \  
&& pecl install imagick \  
&& docker-php-ext-install mysql pdo_mysql zip \  
&& docker-php-ext-enable imagick \  
&& docker-php-ext-enable opcache \  
&& docker-php-ext-enable memcache \  
&& docker-php-ext-enable zip \  
&& php /usr/src/installer && mv /var/www/html/composer.phar
/usr/local/bin/composer \  
&& mkdir -p /var/www/.composer \  
&& chown www-data:www-data /var/www/.composer \  
&& apt-get remove -y \--purge build-essential gcc cpp libmemcached-dev libz-
dev \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/pear \  
&& rm -rf /var/lib/apt/lists/*  

