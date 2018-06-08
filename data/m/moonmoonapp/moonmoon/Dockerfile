FROM php:7.2-apache  
  
MAINTAINER Thomas Chauchefoin <thomas+docker@chauchefoin.fr>  
  
RUN apt-get update && \  
apt-get install -y git unzip --no-install-recommends && \  
git clone https://github.com/moonmoon/moonmoon.git /var/www/html/ && \  
php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');"
&& \  
php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
&& \  
composer install -d /var/www/html/ --no-dev && \  
chown -R www-data:www-data /var/www/html/ && \  
apt-get purge -y git unzip && \  
rm -rf /var/lib/apt/lists/*  

