FROM php:5-apache  
  
ADD files/docker-php-pecl-install /usr/local/bin  
ADD files/php.ini /usr/local/etc/php/php.ini  
  
RUN apt-get update && \  
apt-get install -y zlib1g-dev libicu-dev g++ libxml2-dev zip unzip curl git  
  
RUN docker-php-pecl-install xdebug-2.5.5  
  
RUN docker-php-ext-configure intl && \  
docker-php-ext-install intl mbstring bcmath zip  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php \--install-dir=/usr/bin \--filename=composer && \  
php -r "unlink('composer-setup.php');"  
RUN a2enmod rewrite && service apache2 restart  
  
RUN composer create-project syonix/monolog-viewer /var/www/html  
  
RUN chown -R www-data:www-data /var/www/html

