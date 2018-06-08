FROM gold/apache-php:manual_1  
#FROM tutumcloud/apache-php  
# Image n2ru/monolith  
# Version 0.0.20  
MAINTAINER shuron  
  
RUN a2enmod rewrite #Adding mod rewrite  
#RUN mv /etc/apache2/sites-enabled/000-default.conf /etc/apache2/sites-
enabled/000-default.conf_back  
ADD docker/000-default.conf /etc/apache2/sites-enabled/000-default.conf  
ADD docker/php.ini /etc/php5/apache2/php.ini  
########  
#Volumes  
########  
VOLUME /app/modules/upload/attachments  
VOLUME /app/avatars/  
#Appache logs should be already in base image  
#VOLUME /var/log/apache2  

