FROM golang:1.8-alpine  
  
MAINTAINER Sergii Nuzhdin <ipaq.lw@gmail.com>  
  
ENV GLIDE_VERSION 0.12.3  
ENV GLIDE_DOWNLOAD_URL
https://github.com/Masterminds/glide/releases/download/v${GLIDE_VERSION}/glide-v${GLIDE_VERSION}-linux-
amd64.tar.gz  
  
RUN apk add --update ca-certificates \  
&& apk add curl git coreutils \  
&& rm /var/cache/apk/*  
  
RUN curl -fsSL "$GLIDE_DOWNLOAD_URL" -o glide.tar.gz \  
&& tar -xzf glide.tar.gz \  
&& mv linux-amd64/glide /usr/bin/ \  
&& rm -r linux-amd64 \  
&& rm glide.tar.gz  
  

