FROM alpine:3.6  
  
RUN apk add \--update \  
autoconf \  
automake \  
build-base\  
curl \  
git \  
go \  
libtool \  
protobuf \  
qt5-qtbase-dev  
  
RUN git clone https://github.com/google/protobuf \  
&& cd protobuf \  
&& ./autogen.sh \  
&& ./configure --prefix=/usr \  
&& make \  
&& make check \  
&& make install \  
&& cd .. && rm -rf protobuf && cd  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir /go \  
&& go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway \  
&& go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger \  
&& go get -u github.com/golang/protobuf/protoc-gen-go

