# Build the faucet in a stock Go builder container  
FROM golang:1.9-alpine as builder  
  
RUN apk add --no-cache make gcc musl-dev linux-headers  
  
ADD . /go-ethereum  
RUN cd /go-ethereum && make all  
  
# Pull the faucet into a second stage deploy alpine container  
FROM alpine:latest  
  
RUN apk add --no-cache ca-certificates  
COPY \--from=builder /go-ethereum/build/bin/faucet /usr/local/bin/  
  
EXPOSE 8080 30303 30303/udp  
ENTRYPOINT ["faucet"]  

