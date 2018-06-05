FROM php:7.1-fpm  
  
RUN apt-get update  
RUN apt-get install -yq libpq-dev mysql-client postgresql-client  
RUN docker-php-ext-install pdo_pgsql pdo_mysql  
  
WORKDIR /app  
  
#ENTRYPOINT ["php", "artisan"]  
CMD ["list"]  

