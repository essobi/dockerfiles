FROM golang:1.7  
ENV GO15VENDOREXPERIMENT=1  
# dependencies  
RUN go get github.com/jteeuwen/go-bindata/...  
RUN go get github.com/golang/lint/golint  
RUN go get github.com/tools/godep  
  
# gometalinter  
RUN go get github.com/alecthomas/gometalinter  
RUN gometalinter --install  
  
ENV BASE=/go/src/github.com/komand/plugin-sdk-go  
ADD . /go/src/github.com/komand/plugin-sdk-go  
  
WORKDIR /go/src/github.com/komand/plugin-sdk-go  
RUN make all && make test  

