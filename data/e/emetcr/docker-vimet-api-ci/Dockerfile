FROM golang:1.9  
  
ENV PROTOC_VERSION 3.4.0  
ENV PROTOC_RELEASE
https://github.com/google/protobuf/releases/download/v$PROTOC_VERSION/protoc-$PROTOC_VERSION-
linux-x86_64.zip  
  
RUN apt-get update && apt-get install -y zip \  
# Install protobuf compiler  
&& wget -O /tmp/protoc.zip $PROTOC_RELEASE \  
&& unzip -d /usr/local /tmp/protoc.zip \  
&& apt-get remove \--purge -y zip \  
# Install build tools  
&& go get -u github.com/golang/dep/... \  
&& go get -u github.com/golang/protobuf/protoc-gen-go \  

