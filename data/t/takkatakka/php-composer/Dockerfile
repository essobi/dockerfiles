FROM php:latest  
  
RUN apt-get update && \  
apt-get install git curl zlib1g-dev lftp -yqq && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-install zip && \  
curl --silent --show-error https://getcomposer.org/installer | php && \  
mv composer.phar /bin/composer  
  
RUN composer global require "hirak/prestissimo"  

