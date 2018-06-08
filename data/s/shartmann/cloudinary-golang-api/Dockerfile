FROM golang:alpine  
  
RUN apk update && apk add git  
ADD . /go/src/github.com/ledroide/cloudinary-golang-api  
WORKDIR /go/src/github.com/ledroide/cloudinary-golang-api  
RUN go get github.com/gorilla/mux  
RUN go get github.com/prometheus/client_golang/prometheus  
RUN go get github.com/opentracing/opentracing-go  
RUN go get github.com/openzipkin/zipkin-go-opentracing  
RUN go install github.com/ledroide/cloudinary-golang-api  
  
ENTRYPOINT /go/bin/cloudinary-golang-api  
  
EXPOSE 8090  

