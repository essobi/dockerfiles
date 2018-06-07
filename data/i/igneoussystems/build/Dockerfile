FROM golang:1.3.1-cross  
  
MAINTAINER eng@igneous.io  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y  
RUN apt-get install -y build-essential autoconf libtool  
  
ADD https://github.com/google/protobuf/archive/v3.0.0-alpha-1.tar.gz
/root/protobuf.tar.gz  
RUN bash -c 'cd /root && tar xf protobuf.tar.gz && cd protobuf* &&
./autogen.sh && ./configure --prefix=/usr && make && make install'  
  
RUN bash -c 'go get github.com/golang/protobuf/{proto,protoc-gen-go}'  
RUN bash -c 'go get code.google.com/p/go.tools/cmd/vet'  

