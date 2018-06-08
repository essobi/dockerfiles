FROM php:5-fpm  
  
RUN apt-get update && \  
apt-get install -y -q --no-install-recommends ssmtp && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY mail.ini /usr/local/etc/php/conf.d/  

