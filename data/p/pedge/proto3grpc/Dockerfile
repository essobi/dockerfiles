FROM golang:1.5.1  
MAINTAINER peter.edge@gmail.com  
  
RUN \  
apt-get update -yq && \  
apt-get install -yq --no-install-recommends \  
autoconf \  
automake \  
build-essential \  
git \  
libtool \  
unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
wget https://codeload.github.com/google/protobuf/tar.gz/v3.0.0-beta-3 && \  
tar xvzf v3.0.0-beta-3 && \  
rm v3.0.0-beta-3 && \  
cd protobuf-3.0.0-beta-3 && \  
./autogen.sh && \  
./configure --prefix=/usr && \  
make && \  
make check && \  
make install && \  
cd - && \  
rm -rf protobuf-3.0.0-beta-3  
  
RUN \  
git clone https://github.com/grpc/grpc.git && \  
cd grpc && \  
git submodule update --init && \  
make && \  
make install  
  
RUN \  
go get \  
github.com/golang/protobuf/proto \  
github.com/golang/protobuf/protoc-gen-go \  
google.golang.org/grpc \  
github.com/gengo/grpc-gateway/protoc-gen-grpc-gateway  

