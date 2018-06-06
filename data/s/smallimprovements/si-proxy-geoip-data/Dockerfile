FROM node:7.7.1-alpine  
WORKDIR /tmp  
  
ENV VERSION 20180206  
ADD . .  
  
RUN apk add --update curl && \  
rm -rf /var/cache/apk/*  
  
RUN curl -sSLO
http://geolite.maxmind.com/download/geoip/database/GeoLite2-City-
CSV_${VERSION}.zip && \  
curl -sSLO
http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country-
CSV_${VERSION}.zip && \  
unzip GeoLite2-City-CSV_${VERSION}.zip && unzip GeoLite2-Country-
CSV_${VERSION}.zip && \  
mkdir /geoip-data && \  
npm install && \  
node index \  
GeoLite2-City-*/GeoLite2-City-Blocks-IPv4.csv \  
GeoLite2-City-*/GeoLite2-City-Locations-en.csv \  
city_name > /geoip-data/cities.map && \  
node index \  
GeoLite2-Country-*/GeoLite2-Country-Blocks-IPv4.csv \  
GeoLite2-Country-*/GeoLite2-Country-Locations-en.csv \  
country_iso_code > /geoip-data/countries.map && \  
rm -r ./*  
  
VOLUME ["/geoip-data"]  

