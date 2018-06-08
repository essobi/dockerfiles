FROM php:7.2-apache  
  
WORKDIR /var/www/  
  
EXPOSE 8000  
RUN apt-get update \  
&& apt-get install -y \  
git \  
zlib1g-dev \  
&& docker-php-ext-install \  
bcmath \  
zip \  
&& a2enmod rewrite \  
&& php -r "readfile('http://getcomposer.org/installer');" | php -- --install-
dir=/usr/bin/ --filename=composer  
  
COPY composer.* ./  
  
RUN composer install --prefer-dist --no-dev  
  
RUN chown www-data:www-data .  
  
COPY . .  

