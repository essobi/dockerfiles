#  
# Packer Dockerfile  
#  
# https://github.com/rosstimson/docker-packer  
#  
# AUTHOR: Ross Timson <ross@rosstimson.com>  
# LICENSE: WTFPL - http://wtfpl.net  
#  
# Installs Packer (https://packer.io).  
#  
FROM alpine  
MAINTAINER Ross Timson <ross@rosstimson.com>  
  
ENV PACKER_VERSION 1.0.2  
# Download and install Packer.  
RUN mkdir /tmp/packer \  
&& cd /tmp/packer \  
&& apk add --update bash curl ca-certificates openssh-client git unzip \  
&& curl -O -sS -L
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
\  
&& unzip packer_${PACKER_VERSION}_linux_amd64.zip \  
&& apk del unzip \  
&& mv packer* /usr/local/bin \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/packer  
  
# Define default command.  
CMD ["packer"]  

