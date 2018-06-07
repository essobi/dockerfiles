FROM golang:1.9 as builder  
  
WORKDIR /go/src/github.com/project0/whaleguard/  
  
COPY . .  
RUN go get -v  
  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o whaleguard .  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates iptables ip6tables  
  
WORKDIR /root/  
  
COPY \--from=builder /go/src/github.com/project0/whaleguard/whaleguard .  
  
ENTRYPOINT ["./whaleguard"]

