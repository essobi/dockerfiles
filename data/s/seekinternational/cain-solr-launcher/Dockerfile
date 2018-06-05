FROM php:5.6.21-apache  
  
MAINTAINER GDP CAIN <gdp-cain@seekasia.com>  
  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
&& docker-php-ext-install -j$(nproc) mcrypt  
  
RUN apt-get install -y cron  
  
COPY /launcher/ /var/www/html/  
COPY /crontab/reindex.sh /etc/cron.d/reindex.sh  
RUN chmod +x /etc/cron.d/reindex.sh  
  
CMD /etc/cron.d/reindex.sh && apache2-foreground  

