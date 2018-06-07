FROM debian:7.8  
ADD http://get.influxdb.org/influxdb_0.9.0-rc30_amd64.deb /tmp/influxdb.deb  
  
RUN dpkg -i /tmp/influxdb.deb  
  
EXPOSE 8083 8086  
ENTRYPOINT ["/opt/influxdb/influxd"]  
CMD ["-config=/etc/opt/influxdb/influxdb.conf"]  

