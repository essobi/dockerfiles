FROM golang:alpine AS build-env  
RUN apk add --no-cache git  
RUN CGO_ENABLED=0 GOOS=linux go get -v -ldflags="-s -w"
github.com/zuBux/badbucket/cmd/badbucket/  
RUN mkdir /tmp/thisIsEmpty  
  
FROM alpine:edge AS pack-env  
WORKDIR /  
RUN apk add --no-cache upx  
COPY \--from=build-env /go/bin/badbucket /  
RUN upx --brute badbucket -obadbucket.upx  
  
FROM scratch as scratch-packed  
LABEL maintainer="Glenn 'devalias' Grant <glenn@devalias.net>"  
# Install ca root certificates  
# https://curl.haxx.se/docs/caextract.html  
# http://blog.codeship.com/building-minimal-docker-containers-for-go-
applications/  
ADD https://curl.haxx.se/ca/cacert.pem /etc/ssl/certs/ca-certificates.crt  
COPY \--from=build-env /tmp/thisIsEmpty /tmp  
COPY \--from=pack-env /badbucket.upx /badbucket  
ENTRYPOINT ["/badbucket"]  

