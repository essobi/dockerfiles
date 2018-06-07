FROM alpine:3.6  
  
MAINTAINER erguotou525@gmail.com  
  
RUN apk update && apk add go git libc-dev && mkdir -p /home/go/src
/home/go/bin /home/go/bin  
  
ENV GOPATH /home/go  
ENV GOBIN /home/go/bin  
ENV PATH=$PATH:$GOBIN  
  
WORKDIR /home/go/src  
  
ONBUILD go version  

