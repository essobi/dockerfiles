FROM golang:stretch  
LABEL maintainer "maintainer@spirala.co" description "Private Cloud platform
based on Docker Swarm"  
  
RUN mkdir -p /go/src/github.com/lnsp/spirala  
ADD . /go/src/github.com/lnsp/spirala  
WORKDIR /go/src/github.com/lnsp/spirala  
RUN go-wrapper install  
CMD ["/go/bin/spirala"]  

