FROM golang as builder  
  
WORKDIR /go/src/github.com/dgmann/ma-lookup  
COPY . .  
  
RUN go-wrapper download && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix
cgo -o /lookup .  
  
FROM scratch  
ADD ca-certificates.crt /etc/ssl/certs/  
COPY \--from=builder /lookup /lookup  
  
EXPOSE 80  
ENV QUEUE_HOST=queue REDIS_HOST=redis  
  
ENTRYPOINT ["/lookup"]

