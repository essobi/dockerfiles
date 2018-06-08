FROM oxkipo/apache2-php7  
MAINTAINER Kristian Drucker  
  
COPY . /var/www  
WORKDIR /var/www  
RUN composer install  
RUN chmod -R 777 /var/www  
RUN cp .env.example .env  
  
ENV IMAGE_DRIVER=imagick

