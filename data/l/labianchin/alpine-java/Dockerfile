FROM gliderlabs/alpine:3.2  
RUN apk add --update \  
ca-certificates \  
curl \  
wget \  
git \  
&& rm -rf /var/cache/apk/*  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
ENV JAVA_VERSION 7u79  
ENV JAVA_ALPINE_VERSION 7.79.2.5.5-r0  
  
RUN apk add --update \  
openjdk7=$JAVA_ALPINE_VERSION \  
&& rm -rf /var/cache/apk/*

