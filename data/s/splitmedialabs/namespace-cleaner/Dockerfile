FROM golang:1.9.2-alpine3.7  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash git openssh  
  
RUN mkdir /go/src/cleaner  
COPY . /go/src/cleaner  
WORKDIR /go/src/cleaner  
RUN go get  
# ATTACH ["/bin/sh"]  
  
  
  
CMD go run main.go  
# TAG marcpar/namespace-cleaner:latest  
# PUSH marcpar/namespace-cleaner:latest

