# based on custom slim image  
FROM mecrawlings/php:7.1-apache  
  
# set working directory  
WORKDIR /var/www/localhost/htdocs/  
  
# copy kirby  
COPY ./starterkit /var/www/localhost/htdocs/  
  
# create thumbs folder and set permissions for kirby  
RUN chown -R apache:apache /var/www/localhost/htdocs/ \  
&& chmod -R 755 /var/www/localhost/htdocs/thumbs  

