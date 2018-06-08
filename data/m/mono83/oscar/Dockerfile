FROM golang:1.9.0-alpine3.6 as builder  
WORKDIR /go/src/github.com/mono83/oscar  
COPY . .  
RUN apk add --no-cache git make && \  
make build  
  
FROM busybox:1.27.2  
COPY \--from=builder /go/src/github.com/mono83/oscar/release/oscar_linux
/oscar  
RUN chmod a+x /oscar  
RUN mkdir /data  
VOLUME /data  
  
ENTRYPOINT ["/oscar"]  

