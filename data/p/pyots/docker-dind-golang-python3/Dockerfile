FROM golang:1.10.1-alpine  
  
FROM docker:dind  
  
COPY \--from=0 /usr/local/go /usr/local/go  
RUN mkdir -p /go/src  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN apk add --no-cache python3 python3-dev py3-pip gcc g++ musl-dev  
  
RUN pip3 install docker-compose grpcio  

