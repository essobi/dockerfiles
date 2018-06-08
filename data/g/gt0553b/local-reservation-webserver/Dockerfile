############################################################  
# Dockerfile to build RBBU_CM build container image  
# Based on Ubuntu  
############################################################  
  
#Download base image ubuntu 16.04  
FROM php:7.0-apache  
  
COPY config/php.ini /usr/local/etc/php/  
COPY config/000-server2go.conf /etc/apache2/sites-available/000-default.conf  
ADD server2go-update.tar.gz /var/www/html  
COPY config/docker-php.conf /etc/apache2/conf-available/docker-php.conf  
  
#RUN ln -s phpinfo.php index.php  
  
#Label  
LABEL Description="ATS Webserver" Vendor="STE" \  
Version="0.9" \  
Maintainer="Patrik Williams <patrik.williams@broadcom.com>"  

