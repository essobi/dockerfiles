FROM alpine:3.5  
COPY . /go/src/github.com/forestscribe/collectd-docker  
  
RUN /go/src/github.com/forestscribe/collectd-docker/docker/build.sh  
  
ENTRYPOINT ["/usr/bin/influxdb-docker-collector"]  

