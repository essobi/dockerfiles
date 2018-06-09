FROM php:7.0-apache  
  
RUN apt-get update \  
&& apt-get install -y libpq-dev libsqlite3-dev \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-install pgsql pdo pdo_mysql pdo_pgsql pdo_sqlite  
  
RUN a2enmod rewrite  

