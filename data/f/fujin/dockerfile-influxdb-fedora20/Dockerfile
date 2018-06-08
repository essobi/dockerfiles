FROM fedora:20  
MAINTAINER AJ Christensen <aj@junglist.io>  
  
ADD http://s3.amazonaws.com/influxdb/influxdb-latest-1.x86_64.rpm
/influxdb_latest_amd64.rpm  
RUN rpm -ivh /influxdb_latest_amd64.rpm  
  
COPY config.toml /opt/influxdb/shared/config.toml  
  
EXPOSE 2003 2003/udp 8083 8086  
VOLUME "/opt/influxdb/shared/data/db"  
CMD ["-config=/opt/influxdb/shared/config.toml"]  
ENTRYPOINT ["/usr/bin/influxdb"]  

