FROM golang:1.4  
MAINTAINER Justin C. Miller <justin@devjustinian.com>  
  
RUN go get github.com/tools/godep  
  
ADD . /go/src/github.com/justinian/slackdice  
  
RUN cd /go/src/github.com/justinian/slackdice && godep go install  
  
CMD ["/go/bin/slackdice"]  
  
EXPOSE 8000  

