FROM alpine:3.5  
VOLUME /site  
WORKDIR /site  
  
ENV HUGO_VERSION 0.20.2  
RUN apk add --no-cache curl && \  
curl -fSL
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
| \  
tar -xz -C /tmp && \  
mv /tmp/hugo_${HUGO_VERSION}_linux_amd64/hugo_${HUGO_VERSION}_linux_amd64
/usr/local/bin/hugo && \  
rm /tmp/ -rf && \  
apk del curl  

