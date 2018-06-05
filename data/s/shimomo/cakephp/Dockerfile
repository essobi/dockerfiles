FROM php:7-apache  
LABEL maintainer "yuichi@shimomo.net"  
  
WORKDIR /var/www/html  
  
COPY ./default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN apt-get update && \  
apt-get install -y curl git libicu-dev libpq-dev zlib1g-dev zip && \  
docker-php-ext-install intl mbstring pcntl pdo_mysql pdo_pgsql zip && \  
usermod -u 1000 www-data && \  
usermod -a -G users www-data && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
chown -R www-data:www-data /var/www && \  
a2enmod rewrite  

