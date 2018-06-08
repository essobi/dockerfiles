FROM php:7.2-fpm  
  
RUN apt-get update && \  
apt-get install -y wget git libicu-dev zlib1g-dev  
  
#RUN docker-php-ext-install zip gd  
RUN docker-php-ext-configure intl && \  
docker-php-ext-install intl zip  
  
ADD install_composer.sh /root/install_composer.sh  
RUN chmod +x /root/install_composer.sh && \  
/root/install_composer.sh  
  
ADD php.ini /usr/local/etc/php/php.ini  

