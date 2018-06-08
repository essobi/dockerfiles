FROM golang:1.3  
RUN go get github.com/go-sql-driver/mysql  
  
RUN go get github.com/jessevdk/go-flags  
  
RUN go get github.com/fluent/fluent-logger-golang/fluent  
  
ADD . /go/src/github.com/tobyhughes/shortie  
  
RUN go install github.com/tobyhughes/shortie  
  
ENTRYPOINT /go/bin/shortie  

