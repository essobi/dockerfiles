FROM php:7.1-fpm  
  
# Build V8  
RUN apt-get update && \  
apt-get install -y bzip2 git g++ libicu-dev libmagickwand-dev libpq-dev
zlib1g-dev  
  
# Install PHP extensions  
RUN docker-php-ext-install bcmath exif intl pcntl pdo pdo_mysql pdo_pgsql zip
&& \  
pecl install apcu imagick && \  
docker-php-ext-enable apcu imagick  
  
# Install Composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Dockerize  
ENV DOCKERIZE_VERSION v0.4.0  
RUN curl -SL
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
| tar xzC /usr/local/bin  

