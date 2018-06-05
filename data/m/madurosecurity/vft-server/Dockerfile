FROM golang:1.9.2-alpine as builder  
WORKDIR /go/src/github.com/madurosecurity/vft-server  
COPY . .  
RUN apk update  
RUN apk --no-cache add git  
  
# Build server  
RUN apk add build-base  
WORKDIR /go/src/github.com/madurosecurity/vft-server/cmd/vft-server/  
RUN go get ./...  
RUN go build -o vft-server .  
  
# Install binaries  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/madurosecurity/vft-server/cmd/vft-
server .  
ENTRYPOINT ["/root/vft-server"]  
CMD ["--bind","0.0.0.0:9999"]  

