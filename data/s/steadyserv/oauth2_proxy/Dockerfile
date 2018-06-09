FROM golang:1.9-alpine AS builder  
  
RUN apk --no-cache add git ca-certificates \  
&& go get github.com/bitly/oauth2_proxy  
  
WORKDIR /go/src/github.com/bitly/oauth2_proxy  
  
RUN go get -d -v  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo .  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
COPY \--from=builder /go/src/github.com/bitly/oauth2_proxy/oauth2_proxy
/usr/local/bin/  
  
ENTRYPOINT ["oauth2_proxy"]  

