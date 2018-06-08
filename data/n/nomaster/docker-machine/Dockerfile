FROM golang AS builder  
ENV CGO_ENABLED=0  
ENV GOOS=linux  
RUN go get github.com/docker/machine  
WORKDIR /go/src/github.com/docker/machine  
RUN make build  
  
FROM alpine as certs  
RUN apk --update add ca-certificates  
  
FROM scratch  
WORKDIR /home  
ENV HOME=/home  
ENTRYPOINT ["/go/bin/docker-machine"]  
COPY \--from=certs etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-
certificates.crt  
COPY \--from=builder /go/src/github.com/docker/machine/bin/docker-machine
/go/bin/docker-machine  

