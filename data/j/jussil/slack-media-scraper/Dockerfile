FROM php:7.1.11-cli-alpine  
  
COPY . /service/  
WORKDIR /service  
  
RUN php composer.phar install  
  
ENTRYPOINT ["php", "run.php"]

