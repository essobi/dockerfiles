FROM debian  
  
#ENV INFLUXDB_VERSION 0.10.0-1  
ENV INFLUXDB_VERSION 0.10.2-1  
ENV INFLUXDB_CHECKSUM 9f814bd296663bcef5f85e986a38ad8f  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl ca-certificates && \  
curl -o /tmp/influxdb.deb
https://s3.amazonaws.com/influxdb/influxdb_${INFLUXDB_VERSION}_amd64.deb && \  
dpkg -i /tmp/influxdb.deb && \  
rm /tmp/influxdb.deb && \  
apt-get -y clean && \  
apt-get autoremove --purge -y curl ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
ADD types.db /usr/share/collectd/types.db  
ADD config.toml /config/config.toml  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
ENV PRE_CREATE_DB **None**  
ENV SSL_SUPPORT **False**  
ENV SSL_CERT **None**  
  
# Admin server WebUI  
EXPOSE 8083  
# HTTP API  
EXPOSE 8086  
# Raft port (for clustering, don't expose publicly!)  
#EXPOSE 8090  
# Protobuf port (for clustering, don't expose publicly!)  
#EXPOSE 8099  
VOLUME ["/data"]  
  
CMD ["/run.sh"]  

