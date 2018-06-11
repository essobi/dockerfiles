FROM alpine:3.6  
RUN apk add --no-cache nginx-mod-http-lua nginx-mod-http-geoip curl  
  
# download geoip database  
RUN curl -O
http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz  
RUN gunzip GeoIP.dat.gz  
RUN curl -O
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz  
RUN gunzip GeoLiteCity.dat.gz  
RUN mkdir /etc/nginx/geoip/  
RUN mv GeoIP.dat /etc/nginx/geoip/  
RUN mv GeoLiteCity.dat /etc/nginx/geoip/  
  
COPY ./nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

