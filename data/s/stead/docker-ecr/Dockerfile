FROM alpine:edge  
  
MAINTAINER Mike Stead  
  
RUN apk --no-cache update && \  
apk --no-cache add bash docker ca-certificates openssl git openssh python py-
pip py-setuptools && \  
pip --no-cache-dir install awscli && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /root  

