FROM ubuntu:16.04  
  
MAINTAINER Larry Smith Jr. <mrlesmithjr@gmail.com>  
  
ENV INFLUXDB_VER="1.4.3"  
  
RUN apt-get update && \  
apt-get install -y wget && \  
wget
https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUXDB_VER}_amd64.deb
&& \  
dpkg -i influxdb_${INFLUXDB_VER}_amd64.deb && \  
rm influxdb_${INFLUXDB_VER}_amd64.deb && \  
apt-get -y clean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY influxdb.conf /etc/influxdb/influxdb.conf  
  
VOLUME /var/lib/influxdb  
  
EXPOSE 8086  
  
CMD ["/usr/bin/influxd","-config","/etc/influxdb/influxdb.conf"]  

