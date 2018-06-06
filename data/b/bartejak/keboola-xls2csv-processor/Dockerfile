FROM php:7.1-cli  
  
RUN apt-get update && apt-get install -y \  
git \  
unzip \  
curl \  
libicu-dev \  
libpng-dev \  
\--no-install-recommends && \  
docker-php-ext-install \  
zip \  
sockets \  
mbstring \  
gd \  
intl && \  
apt-get clean  
  
COPY ./docker/php/php.ini /usr/local/etc/php/php.ini  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin/ --filename=composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
COPY . /app  
WORKDIR /app  
RUN composer install --no-dev --no-interaction --no-progress --no-scripts
--optimize-autoloader  
  
CMD ["php", "run.php"]  

