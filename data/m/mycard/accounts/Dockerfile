FROM php:fpm  
  
RUN apt-get update && apt-get install -y libpq-dev libicu-dev  
RUN docker-php-ext-install pdo_pgsql  
  
RUN curl https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN docker-php-ext-install zip pgsql intl  
RUN pecl install redis  
RUN docker-php-ext-enable redis  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY composer.json /usr/src/app/  
COPY composer.lock /usr/src/app/  
  
RUN composer install  
  
COPY . /usr/src/app  

