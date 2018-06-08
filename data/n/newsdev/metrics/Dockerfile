FROM debian:jessie  
  
RUN apt-get update -y && apt-get install -y curl  
  
ENV INFLUXDB_VERSION=0.8.8  
RUN \  
curl -fO
https://s3.amazonaws.com/influxdb/influxdb-$INFLUXDB_VERSION.amd64.tar.gz && \  
tar -xzf influxdb-$INFLUXDB_VERSION.amd64.tar.gz && \  
cp build/influxdb /usr/local/bin && \  
rm -r build influxdb-$INFLUXDB_VERSION.amd64.tar.gz  
  
COPY config.toml /etc/influxdb/config.toml  
COPY types.db.txt /etc/influxdb/collectd-types.db  
  
EXPOSE 8083  
EXPOSE 8086  
EXPOSE 25826  
VOLUME /data/influxdb  
CMD ["influxdb", "-config", "/etc/influxdb/config.toml"]  

