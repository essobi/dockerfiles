FROM golang:1.7beta2-wheezy  
  
ADD . /go/src/sevki.org/cloud/wiki  
  
RUN go get -v sevki.org/cloud/wiki  
  
ENTRYPOINT wiki  
  
EXPOSE 8080

