FROM centos:7  
MAINTAINER domeos  
  
ENV INFLUXDB_VERSION 0.9.2  
LABEL Description="InfluxDB time series database server $INFLUXDB_VERSION" \  
InfluxDbVersion=$INFLUXDB_VERSION  
  
RUN mkdir -p /tmp/influxdb  
ADD
https://s3.amazonaws.com/influxdb/influxdb-${INFLUXDB_VERSION}-1.x86_64.rpm
/tmp/influxdb/influxdb.x86_64.rpm  
  
WORKDIR /tmp/influxdb  
RUN rpm -ivh influxdb.x86_64.rpm && rm *.rpm  
  
VOLUME /var/opt/influxdb  
  
EXPOSE 8083 8086  
ENTRYPOINT ["/opt/influxdb/influxd", "-config",
"/etc/opt/influxdb/influxdb.conf"]  

