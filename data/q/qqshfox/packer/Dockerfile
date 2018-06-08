FROM alpine  
MAINTAINER Hanfei Shen <qqshfox@gmail.com>  
  
ENV PACKER_VERSION 1.1.3  
RUN mkdir /tmp/packer \  
&& cd /tmp/packer \  
&& apk add --update bash curl ca-certificates openssh-client git perl unzip \  
&& curl -O -sS -L
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
\  
&& unzip packer_${PACKER_VERSION}_linux_amd64.zip \  
&& apk del unzip \  
&& mv packer* /usr/local/bin \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/packer  
  
CMD ["packer"]  

