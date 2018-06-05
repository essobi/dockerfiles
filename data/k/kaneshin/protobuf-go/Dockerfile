FROM kaneshin/protobuf:latest  
  
MAINTAINER Shintaro Kaneko <kaneshin0120@gmail.com>  
  
ENV GOPATH /go  
ENV PATH $PATH:$GOPATH/bin  
  
RUN apk add --update go \  
&& rm -rf /var/cache/apk/*  
  
RUN go get -u github.com/golang/protobuf/proto
github.com/golang/protobuf/protoc-gen-go  

