FROM golang:1.9-alpine  
WORKDIR /go/src/github.com/fankserver/docker-mermaid  
COPY . .  
RUN apk add \--no-cache pcre-dev alpine-sdk && \  
go get github.com/fankserver/docker-mermaid/... && \  
go build -a -installsuffix cgo -o app .  
  
FROM alpine:latest  
RUN adduser -D -u 1000 appuser  
USER appuser  
  
# Add api  
COPY \--from=0 /go/src/github.com/fankserver/docker-mermaid/app /app  
  
# This container will be executable  
ENTRYPOINT ["/app"]  

