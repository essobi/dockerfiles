FROM golang:1.9-alpine  
COPY . /go/src/oilme  
VOLUME ["/go/src/oilme/logs"]  
WORKDIR /go/src/oilme  
CMD go run /go/src/oilme/bee.go  

