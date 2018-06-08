FROM ubuntu:14.04  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
ENV INFLUXDB_VERSION=0.9.4  
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget  
RUN wget
http://influxdb.s3.amazonaws.com/influxdb_${INFLUXDB_VERSION}_amd64.deb \  
&& dpkg -i influxdb_${INFLUXDB_VERSION}_amd64.deb \  
&& rm influxdb_${INFLUXDB_VERSION}_amd64.deb  
  
COPY run.sh /run.sh  
COPY influxdb.conf /etc/opt/influxdb/influxdb.conf  
COPY types.db /usr/share/collectd/types.db  
  
EXPOSE 8083  
EXPOSE 8086  
EXPOSE 25826/udp  
  
VOLUME ["/data"]  
  
CMD ["/run.sh"]  

