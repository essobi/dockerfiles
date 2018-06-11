FROM golang:1.10-alpine  
MAINTAINER Raymond Wen  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:$PATH  
  
RUN apk update && apk add zeromq-dev alpine-sdk  
WORKDIR $GOPATH  

