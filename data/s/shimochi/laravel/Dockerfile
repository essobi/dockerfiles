FROM php:7.1-apache  
LABEL maintainer "shimo@project-com.com"  
  
WORKDIR /var/www/laravel  
  
COPY ./default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN apt-get update && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y libgmp10 libgmp-dev libpq-dev libxml2-dev nodejs && \  
update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10 && \  
docker-php-ext-install bcmath gmp mbstring pdo pdo_pgsql pgsql xml zip && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
chown -R www-data:www-data /var/www/laravel && \  
a2enmod rewrite  

