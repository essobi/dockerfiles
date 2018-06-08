FROM golang:1.9.2-alpine as builder  
WORKDIR /go/src/github.com/madurosecurity/vft-agent  
COPY . .  
RUN apk update  
RUN apk --no-cache add git  
  
# Build server  
RUN apk add build-base  
WORKDIR /go/src/github.com/madurosecurity/vft-agent/cmd/vft-agent/  
#RUN go get ./...  
RUN go build -o vft-agent .  
  
# Install binaries  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/madurosecurity/vft-agent/cmd/vft-agent
.  
ENTRYPOINT ["/root/vft-agent"]  

