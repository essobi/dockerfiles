FROM golang:1.6.0  
MAINTAINER ShopKeep Developers <developers@shopkeep.com>  
  
RUN apt-get update && \  
apt-get install -y build-essential && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN go get github.com/tools/godep \  
golang.org/x/tools/cmd/cover \  
github.com/golang/lint/golint \  
golang.org/x/tools/cmd/vet  

