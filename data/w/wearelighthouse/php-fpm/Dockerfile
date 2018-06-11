FROM wearelighthouse/php-fpm:latest  
  
MAINTAINER wearelighthouse <christy@wearelighthouse.com>  
  
RUN apt-get update && apt-get install -y \  
libmagickwand-dev  
RUN pecl install imagick  
RUN docker-php-ext-enable imagick  

