FROM golang:1.10-alpine  
  
MAINTAINER Tim Ehlers <ehlerst@gmail.com>  
  
RUN apk add --no-cache git  
RUN go get -u github.com/ehlerst/polymur/...  
RUN go install github.com/ehlerst/polymur/cmd/polymur-gateway  
  
CMD ["/go/bin/polymur-gateway"]  

