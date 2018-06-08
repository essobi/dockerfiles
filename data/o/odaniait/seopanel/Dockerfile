FROM php:7.0-apache  
MAINTAINER mike@odania-it.com  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends unzip libpng12-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -o spdownload.zip https://www.seopanel.in/spdownload/ && unzip
spdownload.zip && rm spdownload.zip && mv seopanel/* . && rmdir seopanel  
RUN docker-php-ext-install -j$(nproc) gd  
RUN docker-php-ext-install -j$(nproc) mysqli  
  
ADD run.sh /run.sh  
ADD prepare-config.sh /prepare-config.sh  
RUN /prepare-config.sh  
RUN chown -R www-data:www-data /var/www/html  
RUN chmod 666 /var/www/html/config/sp-config.php  
RUN chmod -R 777 /var/www/html/tmp/  
  
CMD ["/run.sh"]  

