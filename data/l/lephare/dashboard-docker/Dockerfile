FROM php:7.0-cli  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends zlib1g-dev \  
&& docker-php-ext-install -j$(nproc) zip  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY symfony /var/www/symfony  
WORKDIR /var/www/symfony  
  
RUN composer install  
  
EXPOSE 80  
CMD php -S 0.0.0.0:80  

