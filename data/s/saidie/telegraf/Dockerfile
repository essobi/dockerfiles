FROM golang:alpine3.7 AS build  
  
RUN apk add --no-cache build-base git && \  
mkdir /build && \  
go get -d github.com/influxdata/telegraf && \  
cd $GOPATH/src/github.com/influxdata/telegraf && \  
make && cp telegraf /build  
  
FROM alpine:3.7  
COPY \--from=build /build/telegraf /usr/bin/telegraf  
  
CMD /usr/bin/telegraf  

