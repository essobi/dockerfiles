FROM ubuntu:12.04  
ARG PROTOBUF_VERSION=2.4.1  
ADD http://archive.ubuntu.com/ubuntu/pool/main/p/protobuf/protobuf-
compiler_${PROTOBUF_VERSION}-1ubuntu2_amd64.deb /tmp/protobuf-compiler.deb  
ADD
http://archive.ubuntu.com/ubuntu/pool/main/p/protobuf/libprotoc7_${PROTOBUF_VERSION}-1ubuntu2_amd64.deb
/tmp/libprotoc7.deb  
ADD
http://archive.ubuntu.com/ubuntu/pool/main/p/protobuf/libprotobuf7_${PROTOBUF_VERSION}-1ubuntu2_amd64.deb
/tmp/libprotobuf7.deb  
  
RUN dpkg -i /tmp/libprotobuf7.deb /tmp/libprotoc7.deb /tmp/protobuf-
compiler.deb && \  
rm /tmp/*.deb  
  
WORKDIR /src  
  
ENTRYPOINT ["/usr/bin/protoc"]  

