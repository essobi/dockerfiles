FROM php:5.6-apache  
  
RUN docker-php-source extract \  
&& apt-get update \  
&& apt-get install libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev nano -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mysql xsl mysqli pdo_mysql
pdo xml \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& a2enmod rewrite \  
&& a2enmod ssl \  
&& docker-php-source delete  

