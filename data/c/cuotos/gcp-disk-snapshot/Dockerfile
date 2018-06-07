FROM golang:alpine as builder  
  
COPY . /go/src/github.com/cuotos/gcp-disk-snapshot  
  
RUN apk --no-cache add git curl && curl
https://raw.githubusercontent.com/golang/dep/master/install.sh | sh  
  
WORKDIR /go/src/github.com/cuotos/gcp-disk-snapshot  
  
RUN dep ensure  
  
RUN go build -o /tmp/snapshot /go/src/github.com/cuotos/gcp-disk-
snapshot/main.go  
  
FROM alpine  
  
RUN apk --no-cache add ca-certificates  
  
COPY \--from=builder /tmp/snapshot /  
  
WORKDIR /  
  
ENTRYPOINT ["/snapshot"]  

