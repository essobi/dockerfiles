FROM golang:1.10-alpine  
RUN apk add --no-cache git  
RUN go get -u github.com/googlecloudplatform/gcsfuse  
  
FROM dtandersen/factorio:stable  
USER root  
RUN apk add --no-cache ca-certificates fuse && rm -rf /tmp/*  
COPY \--from=0 /go/bin/gcsfuse /usr/local/bin  
USER factorio  

