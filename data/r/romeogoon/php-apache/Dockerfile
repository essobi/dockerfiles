From php:5.6.30-apache  
MAINTAINER Olarn Sukasem <olarn@pakgon.com>  
  
RUN apt-get update && apt-get install -y \  
libpq-dev \  
libmcrypt-dev \  
php5-mysql  
  
#Install PDo Driver  
RUN docker-php-ext-install pdo  
  
#Install PDO PGSQL driver  
RUN docker-php-ext-install pdo_pgsql  
  
# Install PDO MySQL driver  
RUN docker-php-ext-install pdo_mysql  
  
# Enable apache mods.  
RUN a2enmod php5  
RUN a2enmod rewrite  
  
WORKDIR /var/www/html/  
  
# Expose apache.  
EXPOSE 80  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

