FROM golang:1.8-alpine  
  
RUN set -ex \  
&& apk update --no-cache \  
# Install needed apks  
&& apk add --no-cache --virtual --update \  
git \  
glide \  
# Cleanup  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  

