FROM golang:1.9-alpine as builder  
RUN apk add --no-cache git make gcc musl-dev linux-headers  
RUN go get -d github.com/ethereumproject/go-ethereum/cmd/geth  
RUN go install github.com/ethereumproject/go-ethereum/cmd/geth  
  
FROM alpine  
  
COPY \--from=builder /go/bin/geth /usr/local/bin  
  
ENTRYPOINT ["geth"]  

