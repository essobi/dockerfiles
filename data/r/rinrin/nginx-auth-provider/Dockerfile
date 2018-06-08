FROM golang:1.10-alpine3.7 AS builder  
ADD . /go/src/github.com/yuichiro-h/nginx-auth-provider  
WORKDIR /go/src/github.com/yuichiro-h/nginx-auth-provider  
RUN go build -ldflags "-s -w" -o bin/nginx-auth-provider -v  
  
FROM alpine  
  
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*  
  
COPY \--from=builder \  
/go/src/github.com/yuichiro-h/nginx-auth-provider/bin/nginx-auth-provider \  
/nginx-auth-provider  
  
ENTRYPOINT ["/nginx-auth-provider"]

