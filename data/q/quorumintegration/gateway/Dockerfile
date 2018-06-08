FROM golang  
MAINTAINER Wilmot Guillaume - Quorums  
  
RUN go get github.com/tools/godep  
  
ADD . /go/src/github.com/quorumsco/gateway  
  
WORKDIR /go/src/github.com/quorumsco/gateway  
  
RUN godep go build  
  
EXPOSE 8080  
ENTRYPOINT ["./gateway"]  

