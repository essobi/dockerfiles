# Build  
FROM golang:1.8-alpine3.6 as builder  
MAINTAINER Xuejie Xiao <xxuejie@gmail.com>  
RUN apk --no-cache add git gcc g++ musl-dev  
RUN go get -u github.com/pressly/goose/cmd/goose  
  
# Run  
FROM alpine:3.6  
MAINTAINER Xuejie Xiao <xxuejie@gmail.com>  
COPY \--from=builder /go/bin/goose /bin/goose  
CMD ["/bin/goose", "--help"]  

