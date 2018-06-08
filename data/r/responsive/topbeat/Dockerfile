FROM phusion/baseimage:0.9.18  
MAINTAINER responsive  
  
ENV TOPBEAT_VERSION=1.2.2  
RUN apt-get update  
RUN apt-get install -y wget \  
&& mkdir -p /opt/topbeat/config  
  
RUN wget -qO-
https://download.elastic.co/beats/topbeat/topbeat-${TOPBEAT_VERSION}-x86_64.tar.gz
| tar xvz -C /opt/topbeat \  
&& ln -s /opt/topbeat/topbeat-${TOPBEAT_VERSION}-x86_64/topbeat
/usr/bin/topbeat  
  
RUN curl -L -O
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz \  
&& mkdir -p /usr/share/GeoIP \  
&& gunzip -c GeoLiteCity.dat.gz > /usr/share/GeoIP/GeoLiteCity.dat  
  
ADD dashboard/ /opt/topbeat/dashboard  
ADD config/ /opt/topbeat/config  
RUN chmod +x /opt/topbeat/config/entrypoint.sh /opt/topbeat/dashboard/load.sh  
  
CMD ["/opt/topbeat/config/entrypoint.sh"]

