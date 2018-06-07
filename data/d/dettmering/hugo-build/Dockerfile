FROM alpine:3.5  
MAINTAINER tilldettmering@gmail.com  
  
ENV HUGO_VERSION 0.41  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit.tar.gz  
  
# Install HUGO  
RUN set -x && \  
apk add --update wget ca-certificates && \  
wget
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
&& \  
tar xzf ${HUGO_BINARY} && \  
rm -r ${HUGO_BINARY} && \  
mv hugo /usr/bin && \  
apk del wget ca-certificates && \  
rm /var/cache/apk/*  

