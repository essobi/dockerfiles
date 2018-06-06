FROM golang:1.7-alpine as gobuild  
COPY . /go/src/github.com/craig-willis/echoserver  
RUN cd /go/src/github.com/craig-willis/echoserver && go build  
  
FROM alpine  
COPY \--from=gobuild /go/src/github.com/craig-willis/echoserver
/usr/local/bin/echoserver  
  

