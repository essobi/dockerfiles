FROM php:7.0-fpm  
  
ADD files/docker-php-pecl-install /usr/local/bin  
ADD files/php.ini /usr/local/etc/php/php.ini  
  
RUN apt-get update && \  
apt-get install -y zlib1g-dev libicu-dev g++ libxml2-dev zip unzip curl git  
  
RUN docker-php-ext-configure intl && \  
docker-php-ext-install intl mbstring pdo pdo_mysql pdo_pgsql bcmath soap zip  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php \--install-dir=/usr/bin \--filename=composer && \  
php -r "unlink('composer-setup.php');"  

