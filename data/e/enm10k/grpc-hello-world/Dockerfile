FROM golang:1.7-alpine  
  
MAINTAINER enm10k <enm10k@gmail.com>  
  
WORKDIR /go/src/google.golang.org/grpc  
RUN apk add \--update \--no-cache git &&\  
git clone https://github.com/enm10k/grpc-go /go/src/google.golang.org/grpc &&\  
go get github.com/golang/protobuf/proto &&\  
go get golang.org/x/net/context &&\  
go get golang.org/x/text &&\  
go install google.golang.org/grpc/examples/helloworld/greeter_server &&\  
go install google.golang.org/grpc/examples/helloworld/greeter_client &&\  
rm -rf /go/src  

