FROM helder/php:5.3  
LABEL maintainer=helder  
  
# Install drush globally  
RUN apt-install mysql-client && \  
docker-php-ext-install pcntl  
RUN gosu www-data composer global require drush/drush:7.*  
  
COPY drush.sh /docker-entrypoint-init.d/  

