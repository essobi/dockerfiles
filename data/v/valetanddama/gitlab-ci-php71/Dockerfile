FROM php:7.1  
MAINTAINER Alexander<valetanddama@gmail.com>  
  
USER root  
  
RUN apt-get update  
RUN apt-get -y install git  
RUN apt-get -y install mysql-client  
RUN apt-get install zip unzip -y  
RUN apt-get install zlib1g-dev -y  
RUN docker-php-ext-install bcmath zip pdo_mysql  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
EXPOSE 80  
CMD ["php", "-a"]

