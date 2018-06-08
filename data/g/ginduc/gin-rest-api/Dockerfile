FROM golang:1.7-alpine  
MAINTAINER gian@dynamicobjx.com  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash git openssh curl coreutils  
RUN go get github.com/tools/godep  
RUN go get github.com/gin-gonic/gin  
  
RUN mkdir -p /go/src/app  
  
CMD go version  
  

