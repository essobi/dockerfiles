FROM php:7.1-cli  
  
# Install extensions  
RUN apt-get update && apt-get install -y libpq-dev  
RUN docker-php-ext-install pdo_pgsql pdo_mysql  
  
ADD ./ /app  
  
WORKDIR /app  

