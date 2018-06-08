FROM php:5-apache  
MAINTAINER Attila Szeremi <attila+webdev@szeremi.com>  
WORKDIR /var/www  
RUN cd /var/www  
  
RUN apt-get update && apt-get install -y \  
# For composer  
zlib1g-dev  
  
# This includes the docker-php-pecl-install executable  
COPY bin/docker-php-pecl-install /usr/local/bin/  
  
# PHP extensions  
RUN docker-php-ext-install \  
mysqli \  
zip  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
COPY composer.json .  
RUN composer install --optimize-autoloader  
  
COPY . .  
  
COPY config/docker/apache.conf /etc/apache2/sites-available/000-default.conf  
  
RUN a2enmod rewrite  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  

