FROM php:5.6.30-apache  
  
COPY index.php .  
  
RUN sed -i -e "s/Timeout 300/Timeout 86400/" /etc/apache2/apache2.conf  

