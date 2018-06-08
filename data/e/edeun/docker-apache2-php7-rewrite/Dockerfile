FROM php:7.1-apache  
MAINTAINER inlee <einable@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
libxml2-dev \  
vim \  
curl \  
wget \  
unzip \  
git \  
&& docker-php-ext-install -j$(nproc) iconv intl xml soap mcrypt opcache pdo
pdo_mysql mysqli mbstring \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride
None/AllowOverride all/' /etc/apache2/apache2.conf  
  
RUN a2enmod rewrite  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
VOLUME ['/var/www/html', '/usr/local/etc/php/conf.d']

