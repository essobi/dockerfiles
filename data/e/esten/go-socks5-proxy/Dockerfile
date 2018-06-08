FROM golang:latest as builder  
WORKDIR /go/src/github.com/s10/go-socks5-server  
COPY . .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags '-s' -o
./bin/socks5-server  
  
FROM scratch  
COPY \--from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/  
COPY \--from=builder /go/src/github.com/s10/go-socks5-server/bin/socks5-server
.  
  
EXPOSE 1080  
ENTRYPOINT ["./socks5-server"]  

