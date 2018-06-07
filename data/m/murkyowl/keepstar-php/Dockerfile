FROM php:7.1-fpm  
  
# PHP necessities \  
RUN docker-php-source extract \  
docker-php-ext-install sqlite3 curl xml \  
& docker-php-source delete  
  
#install Git and Crontab  
RUN apt-get update &&\  
apt-get install -y git-core cron zip unzip  
  
#Clone the main build in  
RUN \  
cd /var/www/ && git clone https://github.com/shibdib/Keepstar.git  
#install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
#Get Composing  
RUN cd /var/www/Keepstar/ && composer install  
# #Change dir ownerships, Takes forever but needed  
RUN chown -Rv www-data:www-data /var/www/Keepstar/  
  
WORKDIR /var/www/Keepstar  
  

