FROM golang:alpine  
MAINTAINER public@omeid.me  
  
ADD . /go/src/github.com/omeid/echo  
RUN go install -x -v github.com/omeid/echo/http/cmd/echo  
ENTRYPOINT ["/go/bin/echo"]  
  
EXPOSE 3000  

