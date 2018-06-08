FROM php:5-apache  
ENV DEBIAN_FRONTEND noninteractive  
RUN touch /usr/local/etc/php/php.ini | echo date.timezone = "Europe/Paris" >
/usr/local/etc/php/php.ini  
  
RUN apt update  
RUN apt upgrade -y  
RUN apt install -y apt-utils  
  
RUN a2enmod rewrite  
  
RUN apt install -y libmcrypt-dev  
RUN docker-php-ext-install mcrypt  
  
RUN apt install -y libicu-dev  
RUN docker-php-ext-install -j$(nproc) intl  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) gd  
  
RUN docker-php-ext-install mysqli  
  

