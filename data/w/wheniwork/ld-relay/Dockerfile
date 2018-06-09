FROM golang:1.8.4 as builder  
WORKDIR /go/src/github.com/launchdarkly/ld-relay/  
COPY . /go/src/github.com/launchdarkly/ld-relay/  
RUN go get github.com/tools/godep  
RUN CGO_ENABLED=0 GOOS=linux godep go build -a -installsuffix cgo -o ldr  
  
FROM alpine:3.6  
RUN apk add --no-cache \  
curl \  
ca-certificates \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
COPY \--from=builder /go/src/github.com/launchdarkly/ld-relay/ldr /usr/bin/  
COPY docker-entrypoint.sh /usr/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 8030  
CMD ["ldr"]

