FROM php:latest  
MAINTAINER Petr Gregor <docker@gregy.cz>  
  
RUN apt-get update \  
&& apt-get install -y git zlib1g-dev\  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install mbstring zip  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  

