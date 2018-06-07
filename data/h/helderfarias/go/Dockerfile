FROM ubuntu  
  
MAINTAINER Helder Guilherme <helderfarias@gmail.com>  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN apt-get update && apt-get -y install git curl vim  
RUN mkdir $GOPATH  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
RUN cd /usr/local && curl https://storage.googleapis.com/golang/go1.4.3.linux-
amd64.tar.gz | tar -zx  
  
WORKDIR $GOPATH  

