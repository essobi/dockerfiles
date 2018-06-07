FROM alpine:3.5  
RUN \  
apk add --no-cache --virtual .build-deps \  
go git musl-dev \  
  
&& mkdir /go \  
&& export GOPATH=/go \  
&& go get github.com/mhausenblas/burry.sh \  
&& cp /go/bin/burry.sh /usr/local/bin/burry \  
&& rm -rf /go \  
  
&& apk del .build-deps  
  
VOLUME ["/data"]  
  
ENV BACKUP_DIR=/data  
ENV ETCD_ADDR=etcd-weave-2379.service.consul:2379  
COPY backup /etc/periodic/daily/backup  
  
CMD [ "crond", "-f" ]  

