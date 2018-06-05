FROM alpine:3.7 as protoc  
  
ENV PROTOC_VER 3.5.1  
RUN cd /tmp && wget
https://github.com/google/protobuf/releases/download/v${PROTOC_VER}/protoc-${PROTOC_VER}-linux-x86_64.zip  
RUN mkdir -p /tmp/protoc && cd /tmp/protoc && unzip
../protoc-${PROTOC_VER}-linux-x86_64.zip  
RUN cd /tmp/protoc && tar czf /tmp/protoc-${PROTOC_VER}-linux-x86_64.tar.gz *  
  
FROM golang:1.10.2  
# install apache-benchmark (ab)  
RUN apt-get update && apt-get install -y --allow-unauthenticated apache2-utils
&& rm -rf /var/lib/apt/lists/*  
  
ENV PROTOC_VER 3.5.1  
COPY \--from=protoc /tmp/protoc-${PROTOC_VER}-linux-x86_64.tar.gz /tmp/  
RUN cd /usr && tar xzf /tmp/protoc-${PROTOC_VER}-linux-x86_64.tar.gz  
  
RUN go get -u -v github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-
gateway \  
github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger \  
github.com/micro/protobuf/proto \  
github.com/micro/protobuf/protoc-gen-go \  
github.com/golang/dep/cmd/dep \  
github.com/rakyll/hey \  
github.com/go-swagger/go-swagger/cmd/swagger \  
github.com/mwitkow/go-proto-validators/protoc-gen-govalidators \  
github.com/gogo/protobuf/protoc-gen-gofast \  
github.com/gogo/protobuf/protoc-gen-gogofast \  
github.com/oxequa/realize  
  
ADD ./call-api.sh /usr/bin/call-api.sh  

