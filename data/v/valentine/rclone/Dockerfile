# Copyright 2017 Valentine C  
  
FROM alpine:3.7  
  
MAINTAINER Valentine C  
  
ENV GOPATH /go  
  
RUN apk add \--update go git musl-dev ca-certificates \  
&& go get github.com/ncw/rclone \  
&& cp /go/bin/rclone /usr/bin \  
&& rm -rf /go \  
&& apk del go git musl-dev \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
CMD ["/bin/sh"]  

