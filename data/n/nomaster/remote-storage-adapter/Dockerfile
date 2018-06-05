FROM golang as builder  
WORKDIR /go  
RUN go get -d -v
github.com/prometheus/prometheus/documentation/examples/remote_storage/remote_storage_adapter  
RUN go build -v
github.com/prometheus/prometheus/documentation/examples/remote_storage/remote_storage_adapter  
  
FROM golang  
COPY \--from=builder /go/remote_storage_adapter .  
ENTRYPOINT ["./remote_storage_adapter"]  

