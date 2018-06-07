FROM graylog2/server:latest  
LABEL maintainer="goeran.poehner@gmail.com"  
LABEL description="Latest Graylog2 with actual GeoLite2 city database for
usage in Graylog2"  
  
RUN mkdir -p /tmp  
ADD http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
/tmp  
RUN tar xf /tmp/GeoLite2-City.tar.gz -C /tmp --strip-components=1  

