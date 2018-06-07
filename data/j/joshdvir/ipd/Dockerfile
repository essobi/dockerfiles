FROM golang:1.8-alpine  
RUN apk --no-cache add ca-certificates bash git  
WORKDIR /root/  
  
RUN go get github.com/martinp/ipd  
  
ADD
http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.mmdb.gz
/root/  
ADD http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz
/root/  
RUN gzip -d GeoLite2-Country.mmdb.gz  
RUN gzip -d GeoLite2-City.mmdb.gz  
  
COPY index.html /root/index.html  
  
EXPOSE 8080  
CMD [ "ipd","--country-db", "GeoLite2-Country.mmdb", "--city-db",
"GeoLite2-City.mmdb", "--port-lookup", "--reverse-lookup", "--log-level",
"debug", "--trusted-header", "X-Forwarded-For", "--template",
"/root/index.html" ]

