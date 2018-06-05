FROM wickedmonkey/base-image  
MAINTAINER Robert Landers <landers.robert@gmail.com>  
  
ENV CONSUL_VERSION=0.5.0 GOMAXPROCS=2 DATACENTER=local MASTER=""  
# Download and install Consul  
RUN apk add --update go git gcc musl-dev && \  
GOPATH=/go go get github.com/hashicorp/consul && \  
cd /bin && \  
GOPATH=/go go build github.com/hashicorp/consul && \  
rm -rf /go && \  
apk del go git gcc musl-dev && \  
rm -rf /var/cache/apk/* && \  
mkdir -p /data/consul  
  
# Add the files  
ADD root /  
  
VOLUME ["/data/consul"]  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 53 53/udp  

