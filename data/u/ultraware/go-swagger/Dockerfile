FROM golang:1.7-alpine  
  
RUN mkdir /root/go  
RUN apk update && apk upgrade && apk add \--no-cache bash git openssh  
RUN go get -u github.com/go-swagger/go-swagger/cmd/swagger  

