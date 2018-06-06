FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y libmcrypt-dev libzip-dev mysql-client
\  
&& docker-php-ext-install mcrypt pdo_mysql zip \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY database /var/www/database  
COPY php.ini /usr/local/etc/php/  
COPY composer.json composer.lock /var/www/  
  
WORKDIR /var/www  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& composer install --no-scripts --optimize-autoloader  
  
COPY . /var/www  
  
RUN chown -R www-data:www-data \  
/var/www/storage \  
/var/www/bootstrap/cache

