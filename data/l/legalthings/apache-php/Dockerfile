FROM php:5.6-apache  
MAINTAINER Sven Stam <sven@legalthings.io>  
  
RUN apt-get update && apt-get install -y \  
libssl-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
zlib1g-dev \  
libicu-dev \  
g++ \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install intl gettext zip bcmath  
  
RUN a2enmod rewrite  
RUN pecl install mongo mongodb && docker-php-ext-enable mongo mongodb  
  
ADD
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.bz2
/tmp/  
  
RUN tar xvjfC /tmp/ioncube_loaders_lin_x86-64.tar.bz2 /tmp/ \  
&& rm /tmp/ioncube_loaders_lin_x86-64.tar.bz2 \  
&& mkdir -p /usr/local/ioncube \  
&& cp /tmp/ioncube/ioncube_loader_*_5.6.so /usr/local/ioncube \  
&& rm -rf /tmp/ioncube  
  
RUN echo "zend_extension = /usr/local/ioncube/ioncube_loader_lin_5.6.so" >
/usr/local/etc/php/conf.d/ext-ioncube.ini  
  
RUN apt-get install -y libsodium-dev  
RUN pecl install libsodium-1.0.6 && \  
echo "extension=libsodium.so" > /usr/local/etc/php/conf.d/ext-sodium.ini  
  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
ADD sample/ /app  
ADD php.ini /usr/local/etc/php/php.ini  

