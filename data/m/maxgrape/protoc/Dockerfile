FROM golang:1.9.3  
  
ENV PROTOBUF_VERSION 3.5.1  
  
RUN go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway \  
&& go get -u github.com/golang/protobuf/protoc-gen-go \  
&& apt-get update \  
&& apt-get install -y curl unzip \  
&& curl -OL
https://github.com/google/protobuf/releases/download/v$PROTOBUF_VERSION/protoc-$PROTOBUF_VERSION-
linux-x86_64.zip \  
&& unzip protoc-$PROTOBUF_VERSION-linux-x86_64.zip -d protoc3 \  
&& mv protoc3/bin/* /usr/local/bin/ \  
&& mv protoc3/include/* /usr/local/include/ \  
&& rm protoc-$PROTOBUF_VERSION-linux-x86_64.zip \  
&& apt-get remove -y curl unzip \  
&& apt-get autoremove -y  
  
CMD protoc --version

