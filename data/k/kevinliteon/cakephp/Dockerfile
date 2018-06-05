FROM php:5-fpm  
  
RUN apt-get update && apt-get install -y git curl zip libicu-dev zlib1g-dev  
RUN docker-php-ext-install intl mbstring pdo_mysql zip pcntl  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
RUN usermod -u 1000 www-data && usermod -a -G users www-data  
  
RUN mkdir -p /var/www/application && chown -R www-data:www-data /var/www/  
WORKDIR /var/www/application

