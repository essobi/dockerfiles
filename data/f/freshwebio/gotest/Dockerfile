# Start from a Debian image with the latest version of Go installed  
# and a workspace (GOPATH) configured at /go.  
FROM golang:1.7.1-alpine  
  
# install git  
RUN apk add \--no-cache git bzr  
  
# Install gocheck for running tests.  
RUN go get gopkg.in/check.v1  
  
# fetch govendor  
RUN go get github.com/kardianos/govendor  
  
# Install the gcc compiler.  
RUN apk add \--no-cache build-base  

