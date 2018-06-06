FROM golang:alpine AS builder  
  
RUN apk add --no-cache git curl  
  
ENV DEP_VERSION 0.3.2  
RUN curl -fsSL -o /usr/local/bin/dep
https://github.com/golang/dep/releases/download/v${DEP_VERSION}/dep-linux-
amd64 && chmod +x /usr/local/bin/dep  
  
WORKDIR /go/src/github.com/gotoolkit/miner  
  
COPY Gopkg.toml Gopkg.lock ./  
RUN dep ensure -vendor-only  
  
COPY . .  
  
RUN go install .  
  
FROM alpine:latest  
RUN apk add --no-cache ca-certificates  
COPY \--from=builder /go/bin/miner /usr/local/bin/miner  
ENTRYPOINT ["miner"]  
CMD ["-h"]

