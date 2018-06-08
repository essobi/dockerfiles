FROM golang:1.9.2-alpine3.6 as builder  
  
COPY . /go/src/github.com/rafaelbenvenuti/miner  
  
RUN go build -o /tmp/miner github.com/rafaelbenvenuti/miner  
  
FROM alpine:3.6  
COPY \--from=builder /tmp/miner /miner  
  
ENTRYPOINT ["/miner"]  

