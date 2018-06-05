FROM alpine:3.4  
ENV PACKER_VERSION 0.11.0  
# Install Ansible  
RUN apk --update add python py-pip openssl ca-certificates && \  
apk --update add --virtual build-dependencies python-dev libffi-dev openssl-
dev build-base && \  
pip install --upgrade pip cffi && \  
pip install awscli && \  
pip install ansible==2.2.1.0 && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/*  
  
# Packer  
RUN apk --update add bash curl openssh-client git unzip && \  
curl -O -sS -L
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
&& \  
unzip packer_${PACKER_VERSION}_linux_amd64.zip -d /usr/local/bin && \  
apk del unzip && \  
rm -rf /var/cache/apk/*  
  
# Custom C Headers for Alpine  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  

