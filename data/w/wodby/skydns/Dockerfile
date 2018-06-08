FROM wodby/base:0.1  
MAINTAINER Wodby <hello@wodby.com>  
  
COPY rootfs /  
  
RUN apk add --update \  
go \  
git \  
mercurial \  
build-base \  
&& mkdir -p /build/src \  
&& export GOPATH="/build" \  
&& go get github.com/skynetservices/skydns \  
&& GOOS=linux GOARCH=amd64 CGO_ENABLED=0 \  
go build --ldflags '-extldflags "-static" -s -w' \  
github.com/skynetservices/skydns \  
&& mv /build/bin/skydns / \  
&& rm -rf /build \  
&& apk del build-base \  
mercurial \  
git \  
go \  
&& rm -rf /var/cache/apk/*

