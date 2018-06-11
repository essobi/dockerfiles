FROM golang:1.4.2  
WORKDIR /sysgo  
ENV GOPATH=/sysgo  
RUN go get github.com/tools/godep  
WORKDIR /go  
ENV GOPATH=/go  
ENV PATH=$PATH:/sysgo/bin:/go/bin  
ENV GO15VENDOREXPERIMENT=1  

