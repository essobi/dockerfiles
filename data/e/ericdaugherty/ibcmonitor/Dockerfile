FROM golang:latest as builder  
RUN go get -d -v github.com/ericdaugherty/ibc/tools/cmd/ibcmonitor/...  
WORKDIR /go/src/github.com/ericdaugherty/ibc/tools/cmd/ibcmonitor  
RUN GOOS=linux go build -a -o ibcmonitor .  
  
FROM alpine:latest  
RUN apk add --no-cache \  
tzdata \  
ca-certificates  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  
WORKDIR /root/  
COPY \--from=builder
/go/src/github.com/ericdaugherty/ibc/tools/cmd/ibcmonitor/ibcmonitor .  
ENTRYPOINT [ "./ibcmonitor" ]  

