FROM alpine:3.6  
  
MAINTAINER Panu Peters "panu@panuel.de"  
  
ENV CONFD_VERSION=0.14.0  
  
RUN apk add \--update \--no-cache --virtual .build-deps go git musl-dev && \  
go get github.com/kelseyhightower/confd && go build -ldflags '-s -w'
github.com/kelseyhightower/confd && mv confd /usr/local/bin && mkdir -p
/etc/confd/{conf.d,templates} && rm -r /root/go && \  
apk del .build-deps && rm -rf /var/cache/apk/*  

