FROM golang:1.7-alpine  
MAINTAINER @cloverstd https://github.com/cloverstd  
  
RUN apk update && \  
apk add gcc linux-headers musl-dev && \  
rm -rf /var/cache/* && \  
echo "http://mirrors.aliyun.com/alpine/v3.4/main" > /etc/apk/repositories && \  
echo "http://mirrors.aliyun.com/alpine/v3.4/community" >>
/etc/apk/repositories  

