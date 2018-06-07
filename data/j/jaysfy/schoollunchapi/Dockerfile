FROM golang:latest  
  
MAINTAINER Mamoru Izuka  
  
ADD . /go/src/bitbucket.org/jaysfy/schoollunchapi/  
  
RUN go install bitbucket.org/jaysfy/schoollunchapi  
  
ENTRYPOINT ["/go/bin/schoollunchapi"]

