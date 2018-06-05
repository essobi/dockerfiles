FROM php:5.6-fpm  
  
MAINTAINER Dietrich Rordorf <dr@ediqo.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
g++ \  
zlib1g-dev \  
libicu-dev \  
libmcrypt-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
git \  
zip \  
unzip \  
mysql-client \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');" \  
&& chmod +x /usr/local/bin/composer \  
&& /usr/local/bin/composer self-update --no-interaction \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install -j$(nproc) intl pdo_mysql mcrypt gd \  
&& apt-get -y remove zlib1g-dev libicu-dev g++ libmcrypt-dev \  
&& rm -rf /var/cache/*  
  
EXPOSE 9000  
  
CMD ["php-fpm"]  

