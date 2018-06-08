FROM php:7.2-apache  
RUN a2enmod rewrite  
  
Run apt-get update -yqq  
Run apt-get install git libcurl4-gnutls-dev libicu-dev libmcrypt-dev libvpx-
dev libjpeg-dev libpng-dev libxpm-dev zlib1g-dev libfreetype6-dev libxml2-dev
libexpat1-dev libbz2-dev libgmp3-dev libldap2-dev unixodbc-dev libpq-dev
libsqlite3-dev libaspell-dev libsnmp-dev libpcre3-dev libtidy-dev -yqq  
  
Run docker-php-ext-install mbstring pdo_mysql curl json intl gd xml zip bz2
opcache  
  
COPY /public /var/www/html/  
COPY / /var/www/  
  
EXPOSE 80  

