FROM golang:alpine as builder  
RUN apk --no-cache --virtual=build-dependencies add git make gcc g++ && \  
go get -v github.com/ymatsiuk/kafka-offset-exporter  
WORKDIR /go/src/github.com/ymatsiuk/kafka-offset-exporter  
RUN GOARCH=amd64 GOOS=linux go build -v -a -ldflags '-extldflags "-static" -s
-w' -o /bin/kafka-offset-exporter .  
  
FROM alpine:3.6  
COPY \--from=builder /bin/kafka-offset-exporter /bin/kafka-offset-exporter  
CMD ["/bin/sh", "-c", "/bin/kafka-offset-exporter -level debug -brokers
${KAFKA_BROKERS} -path /metrics -port 7979 -topics \"^[^_].*\" -groups \".\""]  

