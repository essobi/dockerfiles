FROM alpine:latest  
MAINTAINER youyo  
  
ENV PACKER_VERSION=1.0.0  
RUN apk add --no-cache --update ca-certificates openssl curl py-paramiko
py2-pip ansible && \  
pip install paramiko && \  
wget
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
&& \  
unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/bin/ && \  
rm -f packer_${PACKER_VERSION}_linux_amd64.zip  

