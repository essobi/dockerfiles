FROM golang:1.8.3 as builder  
WORKDIR /go/src/bitbucket.org/ee-book/xxhzdy/  
COPY . /go/src/bitbucket.org/ee-book/xxhzdy/  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o xxhzdy .  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=builder /go/src/bitbucket.org/ee-book/xxhzdy/xxhzdy /bin/  
ENTRYPOINT ["xxhzdy"]  

