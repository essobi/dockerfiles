FROM golang:1.8 as builder  
WORKDIR /go/src/app  
COPY . .  
RUN go-wrapper download # "go get -d -v ./..."  
RUN CGO_ENABLED=0 go-wrapper install -tags=netgo -ldflags="-X
main.BUILD=$(date -u +%Y-%m-%dT%H:%M:%SZ)"  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
WORKDIR /root  
COPY \--from=builder /go/bin/app .  
COPY \--from=builder /go/src/app/bunnyhop.yml /etc/  
CMD ["./app"]  

