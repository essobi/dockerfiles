FROM golang:1.10.1 AS builder  
  
WORKDIR /go/src/github.com/nordicgaming/connectors  
COPY . .  
  
RUN make binary && mv bin/* /binaries  
  
FROM ubuntu  
  
RUN apt-get update && apt-get install -y \  
ca-certificates  
  
COPY \--from=builder /binaries /sbin/connectors  
  
WORKDIR /  
ENV PATH=$PATH:/sbin/connectors  

