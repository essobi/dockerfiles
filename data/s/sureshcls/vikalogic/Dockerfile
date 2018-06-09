FROM php:5.6.29-apache  
  
COPY src/ /var/www/html  
RUN a2enmod rewrite  
RUN docker-php-ext-install pdo pdo_mysql  
RUN docker-php-ext-install mysqli  
RUN apt-get update -y \  
&& apt-get install -y \  
libxml2-dev \  
php-soap \  
&& apt-get clean -y \  
&& docker-php-ext-install soap  
  
COPY php.ini /usr/local/etc/php/  
  
EXPOSE 80  
FROM mysql:5.6  
MAINTAINER Bo-Yi Wu <appleboy.tw@gmail.com>  
  
CMD ["mysqld"]  
  
EXPOSE 3306

