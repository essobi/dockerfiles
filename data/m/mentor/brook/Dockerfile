FROM golang:alpine as builder  
RUN apk add \--update git  
RUN go get github.com/txthinking/brook/cli/brook  
  
  
FROM alpine:latest  
  
COPY \--from=builder /go/bin/brook /brook  
  
USER nobody  
  
ENTRYPOINT [ "/brook" ]

