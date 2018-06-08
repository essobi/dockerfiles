FROM php:7.2-apache  
  
COPY ./ /var/www/html/  
COPY ./docker/000-default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN apt-get update \  
&& docker-php-ext-install mbstring mysqli opcache pdo_mysql  
  
RUN apt-get install --yes zip unzip  
  
### Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN apt-get -y install git-core  
  
WORKDIR /var/www/html  
  
RUN composer install  
### Project Permissions  
RUN chown 1000:1000 -R *  
RUN chown 1000:www-data -R ./public  
  
### Allow symfony packages  
USER 1000  
RUN composer config extra.symfony.allow-contrib true  
  
#RUN pecl install redis-3.1.0 \  
# && pecl install xdebug-2.5.0 \  
# && docker-php-ext-enable redis xdebug  
RUN ls -la  
USER root  
EXPOSE 80

