FROM golang:1.7  
ENV GOBIN $GOPATH/bin  
  
RUN mkdir -p /go/src/app  
COPY shortme-1.2.0 /go/src/app/shortme  
RUN cd /go/src/app  
RUN apt-get update && apt-get install -y git-core curl build-essential openssl
libssl-dev  
RUN cd /go/src/app/shortme && go get ./... && go build -o shortme main.go  
COPY config.conf /go/src/app/shortme/  
  
EXPOSE 3030  
WORKDIR /go/src/app/shortme  
CMD ["./shortme","-c","config.conf"]  

