FROM golang:1.7.1  
# setup  
ENV PROTOBUF_VERSION 3.2.0  
WORKDIR /opt/protoc  
  
# Download the zip with the binary  
ADD
https://github.com/google/protobuf/releases/download/v$PROTOBUF_VERSION/protoc-$PROTOBUF_VERSION-
linux-x86_64.zip .  
  
# install unzip  
RUN apt-get update && apt-get install unzip  
  
# Unzip and place files  
RUN unzip protoc-$PROTOBUF_VERSION-linux-x86_64.zip && \  
mv bin/protoc /usr/local/bin/ && \  
rm -fr bin readme.md  
  
# install go protobuf and grpc  
RUN go get -u github.com/golang/protobuf/protoc-gen-go  
RUN go get -u google.golang.org/grpc  
  
ENTRYPOINT ["/usr/local/bin/protoc", "--proto_path=/opt/protoc/include"]  

