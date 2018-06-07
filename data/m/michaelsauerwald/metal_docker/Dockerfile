FROM php:5.5-apache  
  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_RUN_DIR /var/run/apache2  
  
# Configure PHP  
RUN buildDeps=" \  
libpng12-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libxml2-dev \  
freetype* \  
vim \  
nano \  
php5-curl \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure \  
gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir \  
&& docker-php-ext-install \  
gd \  
mbstring \  
mysqli \  
mcrypt \  
mysql \  
pdo_mysql \  
zip \  
sockets \  
soap \  
&& apt-get purge -y --auto-remove  
  
RUN a2enmod \  
rewrite \  
session \  
ssl  
  
RUN a2ensite \  
000-default \  
default-ssl  
  
RUN usermod -u 1000 www-data  
  
# install phpunit  
RUN curl -o phpunit.phar -L https://phar.phpunit.de/phpunit-4.1.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit  
  
# Make sure the volume mount point is empty  
RUN rm -rf /var/www/html/*  
  

