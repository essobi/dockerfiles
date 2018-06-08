FROM ubuntu:trusty  
MAINTAINER Christian Ulbrich <christian.ulbrich@zalari.de>  
  
RUN apt-get update && apt-get install -y curl  
  
RUN curl -o influxdb_0.8.8_amd64.deb
https://s3.amazonaws.com/influxdb/influxdb_0.8.8_amd64.deb && \  
dpkg -i influxdb_0.8.8_amd64.deb  
  
ADD ./init/run.sh /usr/local/bin  
  
# Admin server WebUI  
EXPOSE 8083  
# HTTP API  
EXPOSE 8086  
VOLUME ["/opt/influxdb/shared/data"]  
  
CMD ["run.sh"]  

