FROM golang:1.10 as builder  
WORKDIR /go/src/github.com/jaden-young/plumb-rabbit-to-mongo/  
COPY . .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/jaden-young/plumb-rabbit-to-mongo/app
.  
ENV RABBIT_URI "amqps://guest:guest@localhost:5672/"  
ENV RABBIT_QUEUE "vici"  
ENV RABBIT_BINDING_KEY "eiffel.#"  
ENV RABBIT_EXCHANGE "eiffel"  
ENV RABBIT_EXCHANGE_TYPE "topic"  
ENV RABBIT_CONSUMER_TAG "plumb-rabbit-to-mongo"  
ENV MONGO_URI "mongodb://localhost/test"  
ENV MONGO_COLLECTION "test"  
CMD ["./app"]

