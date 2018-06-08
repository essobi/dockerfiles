FROM golang:alpine  
  
ADD . /go/src/github.com/splagemann/goaws  
  
RUN go install github.com/splagemann/goaws  
  
ENTRYPOINT ["/go/bin/goaws"]  
  
EXPOSE 4100  

