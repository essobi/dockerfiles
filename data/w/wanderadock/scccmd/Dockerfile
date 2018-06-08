# Builder image  
FROM golang:1.10 AS builder  
RUN curl -fsSL -o /usr/local/bin/dep
https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 \  
&& chmod +x /usr/local/bin/dep  
  
RUN mkdir -p /go/src/github.com/WanderaOrg/scccmd/  
WORKDIR /go/src/github.com/WanderaOrg/scccmd/  
  
COPY Gopkg.toml Gopkg.lock ./  
RUN dep ensure -vendor-only  
  
COPY cmd/ ./cmd  
COPY internal/ ./internal  
COPY pkg/ ./pkg  
COPY main.go .  
  
RUN CGO_ENABLED=0 go build -o bin/scccmd  
  
# Runtime image  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
COPY \--from=builder /go/src/github.com/WanderaOrg/scccmd/bin/scccmd
/app/scccmd  
WORKDIR /app  
  
ENTRYPOINT ["./scccmd"]

