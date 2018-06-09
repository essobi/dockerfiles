FROM php:5.6-cli-jessie  
  
RUN apt-get update \  
&& apt-get install -y git zip unzip ssh-client  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

