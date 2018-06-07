FROM php:7.1.0-apache  
COPY src/ /var/www/html/  
RUN sed -i s/Listen\ 80/Listen\ 1080/g /etc/apache2/ports.conf  
RUN chmod -R 777 /etc/apache2/  
RUN chmod -R 777 /var/run/apache2/  
RUN chmod -R 777 /var/*/apache2/  
RUN chmod -R 777 /var/www/  
RUN chmod -R 777 /var/www/html/  
EXPOSE 1080  
#EXPOSE 80  

