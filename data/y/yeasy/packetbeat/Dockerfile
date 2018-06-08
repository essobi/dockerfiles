# This will install the packetbeat  
FROM phusion/baseimage:latest  
MAINTAINER yeasy@github  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libpcap0.8 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV VERSION=1.0.1 PLATFORM=x86_64  
ENV FILENAME=packetbeat-${VERSION}-${PLATFORM}.tar.gz  
  
RUN curl -L -O https://download.elastic.co/beats/packetbeat/${FILENAME}\  
&& tar xzvf ${FILENAME}  
  
RUN mkdir -p /usr/share/GeoIP \  
&& cd /usr/share/GeoIP/ \  
&& curl -S -L -O
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz \  
&& gzip -d GeoLiteCity.dat.gz \  
&& rm -f GeoLiteCity.dat.gz  
  
ADD packetbeat.yml /etc/packetbeat/packetbeat.yml  
  
WORKDIR packetbeat-${VERSION}-${PLATFORM}  
  
CMD ["./packetbeat", "-e", "-c=/etc/packetbeat/packetbeat.yml"]  

