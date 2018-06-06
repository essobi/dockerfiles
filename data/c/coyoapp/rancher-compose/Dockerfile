FROM golang:1.9 as builder  
WORKDIR /go/src/github.com/rancher/rancher-compose  
  
COPY . ./  
  
RUN go generate  
RUN CGO_ENABLED=0 go build -a -ldflags '-s' -installsuffix cgo -o bin/rancher-
compose .  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/rancher/rancher-compose/bin/rancher-
compose .  
ENTRYPOINT ["/root/rancher-compose"]  

