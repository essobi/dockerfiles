FROM php:7.1-cli  
  
# Install packages  
RUN apt-get update && \  
apt-get install -y \  
zlib1g-dev  
  
# Install needed extensions  
RUN docker-php-ext-install zip  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
# Add cli app  
COPY cli/ /var/www/html/cli/  
  
# Set workdir  
WORKDIR /var/www/html/cli  
  
# Run composer install  
RUN composer clear-cache && \  
composer install -o  
  
# Enable console  
CMD [ "php", "./console.php" ]  

