FROM php:5.6-apache  
  
LABEL version="1.8.3"  
  
WORKDIR /var/www/html/  
RUN curl -L -o rainloop.zip
http://repository.rainloop.net/v2/webmail/rainloop-latest.zip  
RUN apt-get update  
RUN apt-get install -y unzip  
RUN unzip rainloop.zip  
RUN rm -rf rainloop.zip  
RUN chown -R www-data .  
RUN apt-get remove -y unzip  
  
VOLUME /var/www/html/data  

