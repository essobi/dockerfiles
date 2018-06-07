FROM golang:latest  
WORKDIR /go/src/  
RUN go get github.com/mgutz/ansi  
COPY kissfs.go .  
RUN go build -tags netgo -a -v -installsuffix cgo -o kissfs .  
  
FROM alpine:latest  
MAINTAINER isca <igorsca at gmail dot com>  
COPY \--from=0 /go/src/kissfs /kissfs  
CMD ["/kissfs"]  
  

