FROM php:7-apache  
WORKDIR /var/www  
  
ADD . /var/www  
  
RUN ./pirum build html \  
&& find . -maxdepth 1 -type f -name "*.tgz" -exec php -d memory_limit=-1 pirum
add html {} \; \  
&& chown -R www-data:www-data html \  
&& rm *.tgz  

