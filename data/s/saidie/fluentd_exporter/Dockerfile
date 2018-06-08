FROM golang:alpine3.7 AS build  
  
RUN apk add --no-cache git && \  
mkdir /build && \  
go get github.com/V3ckt0r/fluentd_exporter && \  
cd $GOPATH/src/github.com/V3ckt0r/fluentd_exporter && \  
go build fluentd_exporter.go && cp fluentd_exporter /build  
  
FROM alpine:3.7  
COPY \--from=build /build/fluentd_exporter /usr/bin/fluentd_exporter  
  
CMD /usr/bin/fluentd_exporter  

