FROM debian:jessie  
ENV INFLUX_VERSION=0.9.4.1  
RUN apt-get update \  
&& apt-get install -yq wget \  
&& wget -q
http://influxdb.s3.amazonaws.com/influxdb_${INFLUX_VERSION}_amd64.deb \  
&& apt-get purge wget -y --auto-remove \  
&& dpkg -i influxdb_${INFLUX_VERSION}_amd64.deb \  
&& rm -rf /var/lib/apt/lists/*  
ENTRYPOINT ["/opt/influxdb/influxd"]  
EXPOSE 8083 8086  
VOLUME "/var/lib/influxdb"  

