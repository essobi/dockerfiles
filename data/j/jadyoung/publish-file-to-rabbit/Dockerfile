FROM golang:1.10 as builder  
WORKDIR /go/src/github.com/jaden-young/publish-file-to-rabbit/  
COPY . .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/jaden-young/publish-file-to-rabbit/app
.  
COPY data/events.json data/events.json  
COPY wait-for wait-for  
ENV AMQP_HOST localhost  
ENV AMQP_PORT 5672  
ENV EVENTS_FILE data/events.json  
CMD ["/bin/sh", "-c", "./wait-for ${AMQP_HOST}:${AMQP_PORT} \-- ./app"]

