FROM php:5.6-apache  
  
MAINTAINER CREATIVE AREA  
  
ENV PHPMYADMIN_VERSION 4_6_3  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev  
  
RUN docker-php-ext-install mbstring mysqli mcrypt && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
ADD
https://github.com/phpmyadmin/phpmyadmin/archive/RELEASE_${PHPMYADMIN_VERSION}.tar.gz
/tmp/  
  
RUN tar xzf /tmp/RELEASE_${PHPMYADMIN_VERSION}.tar.gz -C /var/www/html
--strip-components=1  
  
COPY .htaccess /var/www/html/.htaccess  
COPY config.inc.php /var/www/html/config.inc.php  
  
RUN apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/RELEASE_${PHPMYADMIN_VERSION}.tar.gz && \  
rm -rf setup  
  
WORKDIR /var/www/html  

