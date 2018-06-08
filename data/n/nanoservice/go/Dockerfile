FROM alpine:3.2  
MAINTAINER Oleksii Fedorov <waterlink000@gmail.com>  
  
RUN apk add --update go  
RUN apk add --update git  
  
RUN mkdir -p /go/src /go/bin && chmod -R 777 /go  
  
ENV GOPATH /go  
ENV PATH /go/bin:$PATH  
  
WORKDIR /go  

