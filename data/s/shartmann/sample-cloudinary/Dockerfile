FROM golang:latest  
  
ADD . /go/src/github.com/abderraoufbensalem/sample-cloudinary  
WORKDIR /go/src/github.com/abderraoufbensalem/sample-cloudinary  
RUN go get github.com/gorilla/mux  
RUN go get github.com/prometheus/client_golang/prometheus  
RUN go get github.com/opentracing/opentracing-go  
RUN go get github.com/openzipkin/zipkin-go-opentracing  
RUN go install github.com/abderraoufbensalem/sample-cloudinary  
  
ENTRYPOINT /go/bin/sample-cloudinary  
  
EXPOSE 8090  

