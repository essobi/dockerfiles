FROM golang:1.8-alpine  
MAINTAINER nownabe <nownabe@gmail.com>  
  
RUN \  
apk add \--update \--no-cache git gcc musl-dev g++ curl make \  
&& go get -u github.com/golang/dep/cmd/dep \  
&& go get github.com/golang/lint/golint  

