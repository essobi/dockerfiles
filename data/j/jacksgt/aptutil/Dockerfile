FROM golang:1.10 as builder  
  
ENV CGO_ENABLED=0 \  
GODEBUG=netdns=go  
  
RUN go get -u github.com/cybozu-go/aptutil/...  
  
RUN apt-get update && \  
apt-get install ca-certificates  
  
FROM scratch  
  
COPY \--from=builder /go/bin/go-apt-cacher /go/bin/go-apt-mirror /  
COPY \--from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/  
  
VOLUME [ "/var/lib/aptutil", "/var/spool/go-apt-mirror", "/var/spool/go-apt-
cacher"]  
  
EXPOSE 3142  
WORKDIR "/var/lib/aptutil"  

