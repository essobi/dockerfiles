FROM php:5.6-apache  
MAINTAINER David Spreekmeester <david@grrr.nl>  
  
ENV APPLICATION_ENV=development  
  
# Export $TERM explicitly to prevent some problems with Fish shell  
ENV TERM linux  
# Add PHP Composer path to current path  
ENV PATH $PATH:./vendor/bin:/home/scripts/  
  
ADD docker/config/php.ini /usr/local/etc/php/  
ADD docker/config/httpd.conf /etc/apache2/apache2.conf  
ADD docker/scripts/install-composer.sh /home/  
ADD docker/scripts/composer-executable /usr/local/bin/composer  
  
WORKDIR /var/www/html  
  
RUN \  
# Create document root directory.  
mkdir -p /var/www/html/public && \  
  
# Update first  
apt -y update && \  
  
# Basics  
apt -y install apt-utils wget && \  
  
# PHP GD library  
apt -y install \  
libpng12-dev \  
libjpeg-dev \  
php5-gd && \  
docker-php-ext-configure gd --with-jpeg-dir=/usr/lib && \  
docker-php-ext-install gd && \  
  
# Install MySql Improved  
apt -y install php5-mysql && \  
docker-php-ext-install pdo_mysql && \  
  
# Install mod_rewrite on Apache  
a2enmod rewrite && \  
  
# Install PHP Composer  
mkdir /home/scripts && \  
cd /home/scripts && \  
sh /home/install-composer.sh && \  
chmod u+x /usr/local/bin/composer && \  
cd -  
EXPOSE 80  

