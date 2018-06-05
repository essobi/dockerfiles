FROM dreischild/php:7.0-apache  
  
# System auf den aktuellen Stand bringen  
# Weitere Programme und Tools installieren die für das Shopware Dev-System
relevant sind  
#  
# PHP Core Extensions iconv, mcrypt, gd und zip installieren  
#  
# Informationen zu den docker-php-ext* Tools:  
# https://github.com/docker-library/docs/tree/master/php  
#  
RUN apt-get update && apt-get install -y \  
wget \  
vim \  
zip \  
unzip \  
mysql-client \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install zip  
  
# PECL Extensions installieren  
# APCU und xdebug  
RUN pecl install apcu \  
&& pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug  
  
# Install Ioncube loader  
RUN mkdir /ioncube && \  
cd /ioncube && \  
wget
https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
&& \  
tar xvf ioncube_loaders_lin_x86-64.tar.gz && \  
cd `php -i | grep extension_dir | cut -d' ' -f 5` && \  
cp /ioncube/ioncube/ioncube_loader_lin_7.0.so . && \  
echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20151012/ioncube_loader_lin_7.0.so" > /usr/local/etc/php/conf.d/00_docker-
php-ext-ioncube_loader_lin_7.0.ini && \  
rm -rf /ioncube/  
  
#Mod rewrite aktivieren  
RUN a2enmod rewrite  
  
# Apache environment Variablen setzen  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
#php.ini Einstellungen  
ADD resources/php.ini /usr/local/etc/php/php.ini  
  
#Available Site Eintrag aus Resource Ordner importieren  
ADD resources/000-default.conf /etc/apache2/sites-available/000-default.conf  

