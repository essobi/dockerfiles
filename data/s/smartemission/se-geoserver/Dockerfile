FROM kartoza/geoserver:2.12.1  
MAINTAINER Gerwin Hulsteijn  
  
ENV TZ Europe/Amsterdam  
  
RUN \  
apt-get update \  
&& apt-get -y install gettext-base \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY geoserver-data/templates /opt/geoserver/templates  
COPY geoserver-data/data /opt/geoserver/data_dir  
  
COPY entry.sh /entry.sh  
RUN chmod +x /entry.sh  
  
CMD /entry.sh

