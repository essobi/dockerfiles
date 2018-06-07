FROM php:7  
MAINTAINER thangtd90@gmail.com  
  
COPY entrypoint.php /scripts/entrypoint.php  
COPY rocketeer.phar /usr/bin/rocketeer  
RUN chmod +x /usr/bin/rocketeer  
  
RUN docker-php-ext-install pcntl  
  
ENTRYPOINT ["php", "/scripts/entrypoint.php"]  

