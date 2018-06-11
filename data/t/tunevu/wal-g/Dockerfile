FROM golang:alpine as builder  
ARG VERSION=v0.1.9  
ENV GOBIN=/usr/local/go/bin/  
  
RUN apk add --no-cache git make  
  
RUN git clone https://github.com/wal-g/wal-g.git  
  
WORKDIR wal-g  
RUN git checkout $VERSION; \  
go get github.com/wal-g/wal-g  
  
RUN make install  
  
FROM alpine:latest  
COPY \--from=builder /usr/local/go/bin/wal-g /bin/  

