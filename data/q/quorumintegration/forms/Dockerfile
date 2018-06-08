FROM golang  
MAINTAINER Daniel Jean-Baptiste - Quorum Impact  
  
RUN go get github.com/tools/godep  
  
ADD . /go/src/github.com/quorumsco/forms  
  
WORKDIR /go/src/github.com/quorumsco/forms  
  
RUN godep go build  
  
EXPOSE 8080  
ENTRYPOINT ["./forms"]  

