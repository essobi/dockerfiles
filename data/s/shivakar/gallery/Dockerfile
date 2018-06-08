FROM golang:latest  
ENV GODEBUG netdns=cgo  
ADD . /go/src/github.com/shivakar/gallery  
WORKDIR /go/src/github.com/shivakar/gallery  
RUN go install  

