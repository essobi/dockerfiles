FROM buildpack-deps:jessie-curl  
  
MAINTAINER Arkii "sqy6@163.com"  
RUN gpg \  
\--keyserver hkp://ha.pool.sks-keyservers.net \  
\--recv-keys 05CE15085FC09D18E99EFB22684A14CF2582E0C5  
  
ENV INFLUXDB_VERSION 0.12.1  
RUN wget -q
https://s3.amazonaws.com/influxdb/influxdb_$INFLUXDB_VERSION-1_amd64.deb.asc
&& \  
wget -q
https://s3.amazonaws.com/influxdb/influxdb_$INFLUXDB_VERSION-1_amd64.deb && \  
gpg --batch --verify influxdb_$INFLUXDB_VERSION-1_amd64.deb.asc
influxdb_$INFLUXDB_VERSION-1_amd64.deb && \  
dpkg -i influxdb_$INFLUXDB_VERSION-1_amd64.deb && \  
rm -f influxdb_$INFLUXDB_VERSION-1_amd64.deb*  
  
EXPOSE 8083 8086 8090 8099 4242 4444/udp 2003 2003/udp 25826  
ENV INFLUXDB_META_DIR=/var/lib/influxdb/meta \  
INFLUXDB_DATA_DIR=/var/lib/influxdb/data \  
INFLUXDB_DATA_WAL_DIR=/var/lib/influxdb/wal  
VOLUME /var/lib/influxdb  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["influxd"]  

