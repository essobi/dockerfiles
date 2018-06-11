FROM golang:alpine3.7 as builder  
  
RUN apk add --no-cache --virtual .build-deps \  
git && \  
go get -u github.com/googlecloudplatform/gcsfuse && \  
mkdir -p /rootfs/usr/local/bin/ && \  
mv $GOPATH/bin/gcsfuse /usr/local/bin/gcsfuse && \  
apk del .build-deps  
  
###  
FROM alpine:3.7  
RUN apk add --no-cache --virtual .run-deps \  
fuse \  
ca-certificates  
  
COPY \--from=builder /usr/local/bin/gcsfuse /usr/local/bin/gcsfuse  
  
ENTRYPOINT ["gcsfuse"]  
CMD ["--help"]  

