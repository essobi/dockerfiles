FROM golang:alpine AS build-env  
WORKDIR /go/src/app  
RUN apk add --no-cache git ca-certificates  
RUN git clone https://github.com/OJ/gobuster.git .  
RUN go get  
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o gobuster  
  
FROM alpine:edge AS pack-env  
WORKDIR /  
RUN apk add --no-cache upx  
COPY \--from=build-env /go/src/app/gobuster /  
RUN upx --brute gobuster -ogobuster.upx  
  
FROM scratch as scratch-packed  
# Install ca root certificates  
# https://medium.com/on-docker/use-multi-stage-builds-to-inject-ca-certs-
ad1e8f01de1b  
COPY \--from=build-env /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-
certificates.crt  
COPY \--from=pack-env /gobuster.upx /gobuster  
ENTRYPOINT ["/gobuster"]  

