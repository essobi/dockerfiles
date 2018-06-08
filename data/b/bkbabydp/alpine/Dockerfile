FROM alpine:3.7  
  
RUN set -eux; \  
sed -i.bak "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g"
/etc/apk/repositories; \  
apk update; \  
apk add \--no-cache git  

