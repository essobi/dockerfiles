FROM php:5.6-cli  
MAINTAINER chxj1992 chxj1992@gmail.com  
  
RUN apt-get update  
RUN apt-get install -qqy curl zip libzip-dev  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=bin
--filename=composer  
  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN docker-php-ext-install zip  
  
RUN composer install --prefer-dist  
RUN chmod -R 777 var  
  
EXPOSE 8000  
CMD ["composer", "run"]  

