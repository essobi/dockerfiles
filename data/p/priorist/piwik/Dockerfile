FROM php:apache  
  
MAINTAINER priorist <contact@priorist.com>  
  
RUN apt-get update && apt-get install -y unzip php5-geoip php5-dev libgeoip-
dev libfreetype6-dev libjpeg62-turbo-dev libpng12-dev  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install mysqli gd mbstring && \  
pecl install geoip  
  
RUN echo 'always_populate_raw_post_data=-1' >> /usr/local/etc/php/php.ini && \  
echo 'extension=geoip.so' >> /usr/local/etc/php/php.ini && \  
echo 'geoip.custom_directory=/var/www/html/misc' >> /usr/local/etc/php/php.ini  
  
ADD init.sh /root/init.sh  
RUN chmod +x /root/init.sh  
  
ADD http://builds.piwik.org/piwik.zip /tmp/piwik.zip  
ADD http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
/tmp/GeoLiteCity.dat.gz  
  
RUN unzip -q /tmp/piwik.zip -d /tmp && \  
gunzip /tmp/GeoLiteCity.dat.gz && \  
mv /tmp/piwik/* /var/www/html/ && \  
mv /tmp/GeoLiteCity.dat /var/www/html/misc/GeoIPCity.dat && \  
chown -R www-data:www-data /var/www/html && \  
rm -r /tmp/*  
  
RUN apt-get remove -y unzip php5-dev libgeoip-dev && \  
apt-get autoremove -y && \  
apt-get autoclean  
  
CMD /root/init.sh && apache2-foreground  

