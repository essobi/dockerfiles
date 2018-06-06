# Build Geth in a stock Go builder container  
FROM golang:1.9-alpine as builder  
  
RUN apk add --no-cache make gcc musl-dev linux-headers curl  
  
ENV VERSION=2.0.1  
RUN curl -L https://github.com/jpmorganchase/quorum/archive/v${VERSION}.tar.gz
| tar -zxf - -C src && \  
mv src/quorum-${VERSION} src/quorum && \  
cd /go/src/quorum && \  
make all  
  
# Pull all binaries into a second stage deploy alpine container  
FROM alpine:latest  
  
RUN apk add --no-cache ca-certificates curl  
COPY \--from=builder /go/src/quorum/build/bin/* /usr/local/bin/  
  
EXPOSE 8545 8546 30303 30303/udp 30304/udp  

