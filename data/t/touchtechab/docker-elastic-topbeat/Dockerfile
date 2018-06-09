FROM alpine:3.4  
MAINTAINER Aurélien Thieriot <aurelien@scalar.is>  
  
ENV TOPBEAT_VERSION=1.2.3  
RUN apk update && \  
apk add \  
ca-certificates \  
curl && \  
rm -rf /var/cache/apk/*  
  
#RUN curl -L -O
https://download.elastic.co/beats/topbeat/topbeat-${TOPBEAT_VERSION}-x86_64.tar.gz
&& \  
# tar -xvvf topbeat-${TOPBEAT_VERSION}-x86_64.tar.gz && \  
# mv topbeat-${TOPBEAT_VERSION}-x86_64/ /etc/topbeat && \  
# mv /etc/topbeat/topbeat.yml /etc/topbeat/topbeat.example.yml && \  
# mv /etc/topbeat/topbeat /bin/topbeat  
ADD bin/topbeat /bin/  
ADD bin/topbeat.template.json /etc/topbeat/  
  
RUN curl -L -O
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz && \  
mkdir -p /usr/share/GeoIP && \  
gunzip -c GeoLiteCity.dat.gz > /usr/share/GeoIP/GeoLiteCity.dat  
  
WORKDIR /topbeat  
  
ADD files/ .  
  
CMD /topbeat/start.sh  

