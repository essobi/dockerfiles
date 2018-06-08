FROM php:apache  
  
RUN a2enmod rewrite  
  
RUN apt-get update \  
&& apt-get install curl php5-cli git -y \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/lib/http-echo/data && chmod -R 777 /var/lib/http-echo  
  
VOLUME /var/lib/http-echo/data/  
  
COPY ./ /var/www/html/  
  
RUN composer update  

