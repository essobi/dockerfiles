FROM php:5.5-apache  
  
RUN apt-get update \  
&& apt-get install -y \  
sendmail \  
libpng-dev \  
zlib1g-dev  
  
RUN docker-php-ext-install gd \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install mysql \  
&& docker-php-ext-install mbstring  

