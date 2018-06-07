FROM golang:1.8.3-alpine  
MAINTAINER WU KAI <kai.wu@darkanchor.com>  
  
RUN apk add -U git curl build-base python-dev autoconf automake libtool unzip
\  
&& go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway \  
&& go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger \  
&& go get -u github.com/golang/protobuf/proto \  
&& go get -u github.com/golang/protobuf/protoc-gen-go \  
&& go get -u google.golang.org/grpc \  
&& curl -sSL https://github.com/google/protobuf/archive/v3.3.1.tar.gz | tar
-xvzC /tmp/ \  
&& cd /tmp/protobuf-3.3.1 && ./autogen.sh && ./configure && make && make
install \  
&& apk del --purge *-dev build-base git \  
&& apk add \--no-cache libstdc++ \  
&& rm -rf /tmp/protobuf-3.3.1 \  
&& rm -rf /var/cache/apk/*  
  
CMD ["protoc"]  

