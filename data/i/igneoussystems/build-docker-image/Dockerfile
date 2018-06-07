FROM golang:1.4.2-cross  
  
MAINTAINER eng@igneous.io  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && apt-get install -y \  
build-essential \  
autoconf \  
libtool \  
cmake \  
python-sphinx \  
genext2fs \  
mtd-tools \  
s3cmd  
  
ADD https://github.com/google/protobuf/archive/v3.0.0-alpha-1.tar.gz
/root/protobuf.tar.gz  
RUN cd /root && tar xf protobuf.tar.gz && cd protobuf* && ./autogen.sh &&
./configure --prefix=/usr && make && make install  
  
# Re-build the standard lib with 'race' and 'netgo' support,  
# so individual builds don't need to touch GOROOT.  
RUN go install -race std  
RUN go install -tags netgo -installsuffix netgo std  
  
RUN go get\  
github.com/golang/protobuf/proto\  
github.com/golang/protobuf/protoc-gen-go\  
golang.org/x/tools/cmd/vet\  
golang.org/x/tools/cmd/cover  

