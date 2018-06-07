FROM python:3-alpine  
  
# add packer  
# https://hub.docker.com/r/rosstimson/packer/~/dockerfile/  
ENV PACKER_VERSION 0.10.0  
# Download and install Packer.  
RUN mkdir /tmp/packer \  
&& cd /tmp/packer \  
&& apk add --update bash curl ca-certificates openssh-client git unzip jq
docker \  
&& curl -O -sS -L
https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
\  
&& unzip packer_${PACKER_VERSION}_linux_amd64.zip \  
&& apk del unzip \  
&& mv packer* /usr/local/bin \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/packer  
  
# install python requirements  
ADD requirements*.txt setup.cfg /tmp/  
WORKDIR /tmp/  
RUN pip --disable-pip-version-check install --no-cache-dir -r requirements.txt  
  
# install tests  
ADD scripts/* /tmp/  
RUN /tmp/install_test.sh  
  
# install tests  
ADD tests/ /opt/tests/  
  
# install resource assets  
ADD assets/ /opt/resource/  
  
# test  
RUN /tmp/test.sh  
RUN /tmp/cleanup_test.sh  

