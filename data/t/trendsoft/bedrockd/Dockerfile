FROM php:7.1.5-apache  
  
RUN apt-get update && apt-get install -y libfreetype6-dev libjpeg62-turbo-dev
libmcrypt-dev libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt && docker-php-ext-configure
gd \--with-freetype-dir=/usr/include/ \--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd mysqli pdo_mysql \  
&& cp /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/ \  
&& mv /var/www/html /var/www/web \  
&& sed -i 's/\/var\/www\/html/\/var\/www\/web/' /etc/apache2/sites-
available/default-ssl.conf \  
&& sed -i 's/\/var\/www\/html/\/var\/www\/web/' /etc/apache2/sites-
available/000-default.conf  
  
WORKDIR /var/www  

