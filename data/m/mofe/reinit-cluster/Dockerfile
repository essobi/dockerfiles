FROM golang:latest as builder  
ADD . /go/src/github.com/MofeLee/reinit-cluster  
WORKDIR /go/src/github.com/MofeLee/reinit-cluster  
RUN go get -u github.com/golang/dep/cmd/dep \  
&& dep ensure \  
&& GOPATH=/go GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build
github.com/MofeLee/reinit-cluster  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/MofeLee/reinit-cluster/reinit-cluster
.  
CMD /root/reinit-cluster  

