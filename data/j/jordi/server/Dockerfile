FROM golang as builder  
WORKDIR /gobuild  
COPY server.go .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o server .  
  
FROM alpine  
LABEL maintainer="Jordi Íñigo"  
RUN apk --no-cache add ca-certificates  
WORKDIR /root/  
COPY \--from=builder /gobuild/server .  
CMD ["./server"]

