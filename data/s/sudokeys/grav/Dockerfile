FROM php:7-apache  
MAINTAINER Bertrand Retif <bertrand@sudokeys.com>  
  
RUN apt-get update && apt-get install -y \  
git \  
ssh-client \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libcurl4-openssl-dev && \  
docker-php-ext-install curl zip && \  
docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ && \  
docker-php-ext-install gd && \  
rm -rf /var/lib/apt/lists/* && \  
a2enmod rewrite  
  
COPY build/php.ini /usr/local/etc/php/  
  
WORKDIR /tmp  
  
RUN git clone -b master https://github.com/getgrav/grav.git /var/www/html && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \  
php -r "unlink('composer-setup.php');" && \  
chmod +x /usr/local/bin/composer  
  
WORKDIR /var/www/html  
  
RUN composer install --no-dev -o && \  
bin/grav install && \  
chown -R www-data:www-data /var/www/html/  
  

