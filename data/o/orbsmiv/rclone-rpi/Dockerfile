# Builder  
FROM golang:1.10-alpine as builder  
  
RUN apk add --no-cache git  
  
ARG version="1.41"  
# get rclone  
RUN git clone https://github.com/ncw/rclone -b "v${version}"
/go/src/github.com/ncw/rclone \  
&& cd /go/src/github.com/ncw/rclone \  
&& git checkout -b "v${version}"  
  
# build rclone  
RUN cd /go/src/github.com/ncw/rclone \  
&& git checkout -f \  
&& env GOOS=linux GOARCH=arm GOARM=7 go build -i -v \  
&& mkdir -p /install \  
&& mv rclone /install  
  
# Final stage  
FROM resin/armhf-alpine:latest  
MAINTAINER orbsmiv@hotmail.com  
  
RUN [ "cross-build-start" ]  
  
RUN apk add --no-cache fuse fuse-dev ca-certificates  
  
# install rclone  
COPY \--from=builder /install/rclone /usr/bin/rclone  
  
CMD [""]  
  
RUN [ "cross-build-end" ]  

