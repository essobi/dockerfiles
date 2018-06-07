FROM composer:latest AS composer  
  
FROM lbosqmsft/mssql-php-msphpsql  
MAINTAINER Webysther <webysther@gmail.com>  
  
COPY \--from=composer /usr/bin/composer /usr/bin/composer  
  
RUN apt-get update && apt-get install -y curl git openssl zip unzip vim tree
wget htop glances  
  
# Composer env  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_ALLOW_SUPERUSER 1  
# Permission  
RUN chmod -R 0777 /tmp  
  
WORKDIR /dimep  
  
RUN git clone \--depth 1 https://github.com/Webysther/dimep.git code  
RUN cd code && composer install --no-progress --no-ansi --no-dev --optimize-
autoloader  
  
ENTRYPOINT ["php", "/dimep/code/bin/dimep", "show"]  

