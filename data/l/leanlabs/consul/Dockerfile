FROM alpine:3.2  
  
RUN apk --update add \  
make \  
git \  
go \  
gcc \  
bash \  
musl-dev \  
openssl-dev && \  
export GOPATH=/go && \  
go get github.com/hashicorp/consul && \  
cd $GOPATH/src/github.com/hashicorp/consul && \  
git checkout v0.5.2 && \  
make && \  
mv bin/consul /usr/local/bin/ && \  
rm -rf $GOPATH && \  
apk del --purge \  
make \  
git \  
go \  
gcc \  
bash \  
musl-dev \  
openssl-dev && \  
mkdir -p /tmp/consul && \  
rm -rf /etc/ssl/certs/* && \  
rm -rf /var/cache/apk/*  
  
COPY config.json /etc/consul/config.json  
  
EXPOSE 8300-8302 8301-8302/udp 8400 8500 53 53/udp  
  
ENTRYPOINT ["consul"]  

