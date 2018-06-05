FROM golang:alpine  
MAINTAINER Christian Höltje <docwhat@gerf.org>  
  
COPY *.go /go/src/github.com/docwhat/docker-image-cleaner/  
  
RUN apk add \--update \--no-cache go git && go get github.com/docwhat/docker-
image-cleaner && apk del go git  
  
ENTRYPOINT ["/go/bin/docker-image-cleaner"]  

