FROM golang:1.8.3-alpine  
  
MAINTAINER Susanna Martinelli <susanna.martinelli@geouniq.com>  
  
ENV GLIDE_VERSION v0.12.3  
RUN set -xe && \  
apk update && \  
apk upgrade && \  
apk add tar && \  
apk add curl && \  
apk add git && \  
apk add openssh-client && \  
curl -Ls
https://github.com/Masterminds/glide/releases/download/${GLIDE_VERSION}/glide-${GLIDE_VERSION}-linux-
amd64.tar.gz | tar -xz --strip-components=1 -C /tmp && \  
mv /tmp/glide /usr/local/bin/ && \  
rm -rf /tmp/*  

