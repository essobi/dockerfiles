FROM ubuntu:14.04.4  
MAINTAINER kaezarrex <dhazinski@gmail.com>  
  
ENV NODEJS_VERSION=4.4.0 \  
PATH=$PATH:/opt/node/bin  
  
WORKDIR "/opt/node"  
  
RUN apt-get -qq update && apt-get -qq install -y curl ca-certificates --no-
install-recommends && \  
apt-get install -y python python-dev python-pip python-virtualenv && \  
curl -sL
https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz
| tar xz --strip-components=1 && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
WORKDIR "/root"  

