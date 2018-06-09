#not using alpine because sqlite requires gcc  
FROM golang:1.8  
ADD . /go/src/github.com/sevki/rehook/  
  
WORKDIR /go/src/github.com/sevki/rehook/  
  
RUN go get github.com/sevki/rehook  
  
CMD rehook  
  
EXPOSE 9000  
EXPOSE 9001

