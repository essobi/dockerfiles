FROM golang:1.6-alpine  
MAINTAINER <nabeken@tknetworks.org>  
  
ENV GIN_MODE=release  
  
RUN apk add --no-cache --update bash git  
  
ADD https://raw.githubusercontent.com/docker-library/golang/master/1.5/go-
wrapper /usr/local/bin/go-wrapper  
RUN chmod 0755 /usr/local/bin/go-wrapper  
  
# pasted from -onbuild  
RUN mkdir -p /go/src/app  
WORKDIR /go/src/app  
  
COPY . /go/src/app  
  
RUN go-wrapper download  
RUN go-wrapper install  
  
CMD ["go-wrapper", "run"]  

