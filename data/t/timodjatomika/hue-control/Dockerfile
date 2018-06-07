FROM php:7.2-apache  
LABEL maintainer="Timo Stankowitz <timo.stankowitz@gmail.com>"  
  
COPY devOps/apache.conf /etc/apache2/sites-available/000-default.conf  
  
RUN mkdir /var/www/timo-hue/  
COPY public /var/www/timo-hue/public  
COPY include /var/www/timo-hue/include

