FROM ubuntu:trusty  
  
MAINTAINER support@lastbackend.com  
  
# Setup curl dependency  
RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf
/var/lib/apt/lists  
  
# Install InfluxDB  
ENV INFLUXDB_VERSION 0.8.8  
RUN apt-get update && \  
apt-get install -y pwgen  
RUN curl -s -o /tmp/influxdb_latest_amd64.deb
https://s3.amazonaws.com/influxdb/influxdb_${INFLUXDB_VERSION}_amd64.deb && \  
dpkg -i /tmp/influxdb_latest_amd64.deb && \  
rm /tmp/influxdb_latest_amd64.deb && \  
rm -rf /var/lib/apt/lists/*  
  
ADD config.toml /config/config.toml  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
ENV PRE_CREATE_DB **None**  
ENV SSL_SUPPORT **False**  
ENV SSL_CERT **None**  
  
# Admin server  
EXPOSE 8083  
# HTTP API  
EXPOSE 8086  
# HTTPS API  
EXPOSE 8084  
# Raft port (for clustering, don't expose publicly!)  
#EXPOSE 8090  
# Protobuf port (for clustering, don't expose publicly!)  
#EXPOSE 8099  
VOLUME ["/data"]  
  
CMD ["/init.sh"]

