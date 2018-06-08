FROM php:7.1-apache  
  
RUN apt-get update \  
&& apt-get install -y vim locales locales-all libfreetype6-dev
libjpeg62-turbo-dev libmcrypt-dev libpng12-dev zziplib-bin msmtp\  
&& a2enmod rewrite \  
&& a2enmod ssl \  
&& docker-php-ext-install mysqli pdo_mysql iconv mcrypt zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& mkdir /var/www/pw-secure  
  
ENV LC_ALL en_US.utf8  
ENV LANG en_US.utf8  
ENV LANGUAGE en_US.utf8  
  
EXPOSE 80  
EXPOSE 443  
VOLUME ["/var/www/html", "/var/www/pw-secure"]  

