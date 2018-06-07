from buildpack-deps:jessie-curl  
  
ENV VERSION 0.13.0  
RUN wget
https://dl.influxdata.com/influxdb/releases/influxdb_${VERSION}_amd64.deb \  
&& dpkg -i influxdb_${VERSION}_amd64.deb \  
&& rm influxdb_${VERSION}_amd64.deb  
  
COPY config.toml /config.toml  
  
# Admin server WebUI  
EXPOSE 8083  
# HTTP API  
EXPOSE 8086  
VOLUME ["/data"]  
  
CMD ["influxd", "-config", "/config.toml"]  

