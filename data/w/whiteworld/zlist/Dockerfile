# zlist  
#  
# VERSION 1.0  
FROM golang  
MAINTAINER whiteworld <ljq258@gmail.com>  
  
## for debug  
#ADD . /go/src/github.com/zlisthq/zlist  
RUN go get github.com/zlisthq/zlist  
  
EXPOSE 8080  
WORKDIR /go/src/github.com/zlisthq/zlist  
ENTRYPOINT /go/bin/zlist  

