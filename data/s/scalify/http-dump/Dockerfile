FROM golang:1.9.2 as builder  
WORKDIR /go/src/github.com/scalify/http-dump/  
  
COPY . ./  
RUN CGO_ENABLED=0 go build -a -ldflags '-s' -installsuffix cgo -o bin/load-
test http_dump.go  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
COPY \--from=builder /go/src/github.com/scalify/http-dump/bin/load-test .  
RUN chmod +x load-test  
ENTRYPOINT ["./load-test"]  

