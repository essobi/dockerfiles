FROM golang:1.9.2-alpine3.6  
  
ENV PROTOC_VERSION 3.5.0  
ENV PATH $PATH:/usr/local/protoc/bin  
  
RUN adduser -D -u 1000 golang  
RUN apk add \--no-cache \  
git \  
curl\  
unzip \  
make \  
ca-certificates \  
&& curl -o tmp.zip -L
https://github.com/google/protobuf/releases/download/v$PROTOC_VERSION/protoc-$PROTOC_VERSION-
linux-x86_64.zip \  
&& mkdir -p /usr/local/protoc \  
&& unzip tmp.zip -d /usr/local/protoc \  
&& rm -rf tmp.zip  
  
RUN go get google.golang.org/grpc \  
&& go get -u github.com/golang/protobuf/protoc-gen-go \  
&& curl https://glide.sh/get | sh \  
&& chown -R golang:golang $GOPATH  
  
USER golang  

