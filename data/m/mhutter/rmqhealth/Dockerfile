FROM golang:alpine as builder  
  
WORKDIR /go/src/github.com/mhutter/rmqhealth  
COPY . .  
RUN CGO_ENABLED=0 go build -a -o /app cmd/rmqhealth/main.go  
  
FROM alpine:latest  
  
ENV PORT 8080  
EXPOSE $PORT  
  
COPY \--from=builder /app /app  
  
RUN set -x && \  
apk add \--no-cache ca-certificates && \  
chmod 755 /app  
  
USER 4242  
ENTRYPOINT ["/app"]  

