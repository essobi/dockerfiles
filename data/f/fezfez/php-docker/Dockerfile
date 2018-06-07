FROM php:5.6-apache  
  
# Install PDO MySQL driver  
# See https://github.com/docker-library/php/issues/62  
RUN apt-get update && apt-get install -y libicu-dev zlib1g-dev  
  
RUN docker-php-ext-install pdo  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-configure intl  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install zip  
  
RUN curl --insecure https://getcomposer.org/composer.phar -o /usr/bin/composer
&& chmod +x /usr/bin/composer  
  
# Workaround for write permission on write to MacOS X volumes  
# See https://github.com/boot2docker/boot2docker/pull/534  
RUN usermod -u 1000 www-data  
  
# Enable Apache mod_rewrite  
RUN a2enmod rewrite  
  
WORKDIR /var/www  

