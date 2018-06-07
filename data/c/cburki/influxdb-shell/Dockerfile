FROM debian:jessie  
MAINTAINER Christophe Burki, christophe.burki@gmail.com  
  
ENV INFLUXDB_VERSION 1.3.2  
# Install influxdb  
ADD
https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUXDB_VERSION}_amd64.deb
/tmp/influxdb_amd64.deb  
RUN dpkg -i /tmp/influxdb_amd64.deb  
  
ENTRYPOINT ["/usr/bin/influx"]  

