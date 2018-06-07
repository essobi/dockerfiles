FROM golang:latest AS build  
ADD . /go/src/distributed-wrk  
WORKDIR /go/src/distributed-wrk  
RUN CGO_ENABLED=0 GOOS=linux go install -a -installsuffix cgo ./...  
  
FROM alpine:3.7  
RUN mkdir /app  
RUN apk add --update wrk  
COPY \--from=build /go/bin/distributed-wrk /app/  
  
WORKDIR /app  
CMD ["./distributed-wrk", "-mode=worker"]  

