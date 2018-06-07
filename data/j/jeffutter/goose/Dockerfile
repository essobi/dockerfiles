FROM golang:1.5  
MAINTAINER jeff@jeffutter.com  
  
RUN go get bitbucket.org/liamstask/goose/cmd/goose  
  
RUN mkdir /db  
WORKDIR /  
  
VOLUME ["/db"]  
  
ENTRYPOINT ["/go/bin/goose"]  
CMD ["status"]  

