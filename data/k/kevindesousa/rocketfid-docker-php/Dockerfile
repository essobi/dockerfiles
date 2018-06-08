FROM php:7.2-fpm-stretch  
  
MAINTAINER Kevin DE SOUSA <contact@kevindesousa.me>  
  
RUN apt-get update && apt-get install -y \  
openssl \  
git \  
unzip \  
curl  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
# Set timezone  
RUN ln -snf /usr/share/zoneinfo/Europe/Paris /etc/localtime && echo
Europe/Paris > /etc/timezone  
RUN printf '[PHP]\ndate.timezone = "%s"\n', Europe/Paris >
/usr/local/etc/php/conf.d/tzone.ini  
RUN "date"  

