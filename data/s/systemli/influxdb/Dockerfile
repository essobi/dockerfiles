FROM ubuntu:14.04  
MAINTAINER louis <louis@systemli.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV INFLUXDB_VERSION 0.8.8  
RUN apt-get update && apt-get install -y curl && \  
curl -s -o /tmp/influxdb_latest_amd64.deb
https://s3.amazonaws.com/influxdb/influxdb_${INFLUXDB_VERSION}_amd64.deb && \  
dpkg -i /tmp/influxdb_latest_amd64.deb && \  
mkdir /config && \  
curl -s -o /config/types.db
https://raw.githubusercontent.com/collectd/collectd/22d5f76d3379a5f61873c52363116ee4ba67afa4/src/types.db
&& \  
rm /tmp/influxdb_latest_amd64.deb && \  
rm -rf /var/lib/apt/lists/*  
  
ADD config.toml.default /config/config.toml.default  
ADD run.sh /run.sh  
  
# admin  
EXPOSE 8083  
# api  
EXPOSE 8086  
#raft  
EXPOSE 8090  
#protobuf  
EXPOSE 8099  
# graphite  
EXPOSE 2003  
# collectd  
EXPOSE 25826  
VOLUME ["/data", "/config"]  
  
CMD /run.sh  

