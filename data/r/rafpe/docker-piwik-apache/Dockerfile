FROM tutum/apache-php  
  
RUN rm -rf /app/*  
RUN curl -L -O https://builds.piwik.org/latest.tar.gz && \  
tar --strip 1 -xzf latest.tar.gz && \  
rm latest.tar.gz  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
php5-geoip php5-dev libgeoip-dev && apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN echo "extension=geoip.so" >> /etc/php5/apache2/php.ini  
RUN echo "geoip.custom_directory=/app/misc" >> /etc/php5/apache2/php.ini  
WORKDIR /app/misc  
RUN curl -L -O
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
&& gunzip GeoIP.dat.gz  
RUN curl -L -O
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz &&
gunzip GeoLiteCity.dat.gz && mv GeoLiteCity.dat GeoIPCity.dat  
RUN chmod a+w /app/config  
  
EXPOSE 80  
VOLUME /app/config  
CMD ["/run.sh"]  

