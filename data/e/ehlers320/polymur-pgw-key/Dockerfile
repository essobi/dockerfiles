FROM golang:1.8.1-alpine  
  
MAINTAINER Tim Ehlers <ehlerst@gmail.com>  
  
RUN apk add --no-cache git  
RUN go get -u github.com/jamiealquiza/polymur/...  
RUN go install github.com/jamiealquiza/polymur/cmd/utils/pgw-key  
  
CMD ["/go/bin/pgw-key"]  

