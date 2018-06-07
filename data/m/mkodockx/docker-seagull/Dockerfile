FROM golang:1.4  
MAINTAINER Markus Kosmal mko-x <code@m-ko-x.de>  
  
RUN go get github.com/astaxie/beego  
  
ADD . /go/src/github.com/tobegit3hub/seagull/  
WORKDIR /go/src/github.com/tobegit3hub/seagull/  
RUN go build seagull.go  
  
EXPOSE 80  
CMD ["./seagull"]  

