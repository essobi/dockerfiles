FROM php:7-fpm  
MAINTAINER Or Poran <or@crazylister.com>  
  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get update && apt-get install -y mlocate nodejs git-all bzip2 --fix-
missing --no-install-recommends  
RUN npm install -g bower  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install pdo  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install opcache  
  
COPY scripts/build_php_redis_extension.sh ./  
RUN chmod a+x ./build_php_redis_extension.sh  
RUN ./build_php_redis_extension.sh  
  
RUN chmod -fR a+r / || :  
RUN chmod -fR a+w / || :  
  

