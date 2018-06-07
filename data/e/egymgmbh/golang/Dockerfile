FROM ubuntu:bionic AS build-env  
  
RUN apt-get update && apt-get install -y ca-certificates  
  
# tools  
RUN apt-get install -y git curl  
  
# go  
RUN apt-get install -y golang go-dep  
ENV GOPATH /root/go  
ENV PATH $PATH:$GOPATH/bin  
  
# golint to measure code quality  
RUN go get -u github.com/golang/lint/golint  
  
# vgo (experimental)  
RUN mkdir /usr/lib/go/api && \  
touch /usr/lib/go/api/go1.10.txt && \  
go get -u golang.org/x/vgo  
  
# protobuf  
RUN apt-get install -y libprotobuf-dev golang-goprotobuf-dev  

