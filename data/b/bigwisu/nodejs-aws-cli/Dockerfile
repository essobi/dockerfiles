FROM node:8.11  
  
MAINTAINER Wisu Suntoyo <bigwisu@gmail.com>  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \--no-install-recommends \  
build-essential g++ python2.7 python2.7-dev unzip curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /tmp \  
&& cd /tmp \  
&& curl -O https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& pip install awscli \  
&& rm -f /tmp/get-pip.py  
ENV JQ_VERSION='1.5'  
RUN wget \--no-check-certificate
https://raw.githubusercontent.com/stedolan/jq/master/sig/jq-release.key -O
/tmp/jq-release.key && \  
wget \--no-check-certificate
https://raw.githubusercontent.com/stedolan/jq/master/sig/v${JQ_VERSION}/jq-
linux64.asc -O /tmp/jq-linux64.asc && \  
wget \--no-check-certificate
https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64
-O /tmp/jq-linux64 && \  
gpg \--import /tmp/jq-release.key && \  
gpg \--verify /tmp/jq-linux64.asc /tmp/jq-linux64 && \  
cp /tmp/jq-linux64 /usr/bin/jq && \  
chmod +x /usr/bin/jq && \  
rm -f /tmp/jq-release.key && \  
rm -f /tmp/jq-linux64.asc && \  
rm -f /tmp/jq-linux64  
  
RUN mkdir ~/.aws

