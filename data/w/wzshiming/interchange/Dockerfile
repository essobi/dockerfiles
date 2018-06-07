  
FROM wzshiming/golang:latest AS builder  
RUN go get -v -u github.com/wzshiming/interchange/cmd/interchange  
  
FROM wzshiming/base:latest  
LABEL Maintainer="wzshiming@foxmail.com" Name=interchange Version=0.0.1  
COPY \--from=builder /tmp/bin/interchange /usr/local/bin/interchange  

