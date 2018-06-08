FROM golang:1.9.0-alpine3.6  
MAINTAINER Christopher Maier <christopher.maier@gmail.com>  
  
ENV GOPATH /gopath  
ENV PATH=${GOPATH}/bin:${PATH}  
  
WORKDIR /gopath/src/github.com/operable/go-relay  
COPY . /gopath/src/github.com/operable/go-relay  
  
RUN apk -U add --virtual .build_deps \  
git make && \  
  
go get -u github.com/kardianos/govendor && \  
make exe && \  
  
mv _build/relay /usr/local/bin && \  
mkdir -p /usr/local/etc && \  
cp docker/relay.conf /usr/local/etc/relay.conf && \  
  
# Provide a place to dump log files, etc.  
mkdir -p /var/operable/relay && \  
  
apk del .build_deps && \  
rm -Rf /var/cache/apk/* && \  
rm -Rf $GOPATH  
  
  
FROM alpine:3.6  
RUN mkdir -p /var/operable/relay  
COPY \--from=0 /usr/local/bin/relay /usr/local/bin  
COPY \--from=0 /usr/local/etc/relay.conf /usr/local/etc/relay.conf  

