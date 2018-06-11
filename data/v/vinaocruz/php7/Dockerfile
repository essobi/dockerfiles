FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y zlib1g-dev libicu-dev g++  
RUN docker-php-ext-configure intl  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install pdo_mysql  
  
RUN apt-get install -y libfreetype6-dev  
RUN apt-get install -y libgd-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr  
RUN docker-php-ext-install gd  
  
RUN apt-get install -y libcurl4-openssl-dev  
RUN docker-php-ext-install curl  
  
RUN apt-get install -y libmcrypt-dev  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install gettext mbstring  
  
RUN docker-php-ext-install zip  

