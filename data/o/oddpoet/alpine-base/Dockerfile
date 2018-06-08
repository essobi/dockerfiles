#==============================================================================  
# alpine-base  
#==============================================================================  
FROM alpine:3.6  
MAINTAINER yunsang.choi<oddpoet@gmail.com>  
  
ENV ALPINE_VERSION 3.6  
# Install basic tools  
RUN apk --update add curl tar zip unzip bash shadow && \  
curl -Ls https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.25-r0/glibc-2.25-r0.apk > /tmp/glibc-2.25-r0.apk &&
\  
apk add --allow-untrusted /tmp/glibc-2.25-r0.apk && \  
chsh root -s /bin/bash  

