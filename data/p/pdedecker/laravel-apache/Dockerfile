# Use the official PHP 5.6 Docker image with Apache  
FROM php:5.6-apache  
  
# Install composer (see Laravel docs)  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install dependencies of the Laravel installer and the PHP plugins  
RUN apt-get update && apt-get install -y git\  
zlib1g-dev  
  
# Install necessary PHP plugins  
RUN docker-php-ext-install pdo mbstring tokenizer zip  
  
# Install the Laravel installer  
RUN composer global require "laravel/installer=~1.1"  
ENV PATH ~/.composer/vendor/bin/:$PATH  
  
# Apache setup: enable mod_rewrite  
RUN a2enmod rewrite

