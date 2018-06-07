FROM ubuntu:14.04  
MAINTAINER Hans Donner  
# Based on https://github.com/tutumcloud/influxdb/blob/master/0.9/Dockerfile  
ENV INFLUXDB_VERSION 0.9.4.2  
RUN apt-get update && \  
apt-get install -y curl && \  
curl -o /tmp/influxdb_latest_amd64.deb
http://s3.amazonaws.com/influxdb/influxdb_${INFLUXDB_VERSION}_amd64.deb && \  
dpkg -i /tmp/influxdb_latest_amd64.deb && \  
rm /tmp/influxdb_latest_amd64.deb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD config.toml /config/config.toml  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
ENV PRE_CREATE_DB **None**  
ENV SSL_SUPPORT **False**  
ENV SSL_CERT **None**  
  
# Admin server  
EXPOSE 8083  
# HTTP API  
EXPOSE 8086  
VOLUME ["/data"]  
  
CMD ["/run.sh"]

