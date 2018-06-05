FROM golang:1.9-alpine  
LABEL maintainer "terje@offpiste.org"  
  
ENV INFLUXDB_URL=http://influxdb:8086/  
ENV INFLUXDB_DATABASE=prometheus  
ENV INFLUXDB_RETENTION_POLICY=autogen  
ENV INFLUXDB_USER=influx  
ENV INFLUXDB_PW=influx  
  
EXPOSE 9201  
COPY run.sh /  
  
RUN apk add --no-cache git && \  
mkdir -p /go/src/github.com/prometheus && \  
cd /go/src/github.com/prometheus && \  
git clone https://github.com/prometheus/prometheus.git && \  
cd
/go/src/github.com/prometheus/prometheus/documentation/examples/remote_storage/remote_storage_adapter
&& \  
go-wrapper download && \  
go-wrapper install && \  
cd / && \  
apk del git && \  
rm -rf /go/src/github.com /var/cache/apk  
  
CMD ["/run.sh"]  

