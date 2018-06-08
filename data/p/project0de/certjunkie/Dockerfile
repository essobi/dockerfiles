FROM golang:1.9 as builder  
  
WORKDIR /go/src/github.com/project0/certjunkie/  
  
COPY . .  
RUN go get -v  
  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o certjunkie .  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
  
WORKDIR /root/  
  
COPY \--from=builder /go/src/github.com/project0/certjunkie/certjunkie .  
  
ENTRYPOINT ["./certjunkie"]

