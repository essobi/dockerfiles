FROM golang:1.8-alpine  
MAINTAINER sat0shi  
  
RUN apk update && apk add git \  
&& go get -u github.com/golang/lint/golint \  
&& rm -rf /var/cache/apk/*  
  

