FROM golang:1.8.1  
ENV BASE=/go/src/github.com/komand/plugin-sdk-go2  
ADD . /go/src/github.com/komand/plugin-sdk-go2  
  
WORKDIR /go/src/github.com/komand/plugin-sdk-go2  
  
RUN make deps && make build && make check && make test

