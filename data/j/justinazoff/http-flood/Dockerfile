# http_flood  
#  
# VERSION 0.1  
FROM golang:alpine  
MAINTAINER Justin Azoff <justin.azoff@gmail.com>  
  
WORKDIR /go/src/github.com/JustinAzoff/http_flood/  
ADD . /go/src/github.com/JustinAzoff/http_flood/  
  
RUN apk add --update git  
RUN go get  
RUN go build  
RUN find /go  
  
EXPOSE 7070  
ENTRYPOINT ["/go/bin/http_flood", "server"]  

