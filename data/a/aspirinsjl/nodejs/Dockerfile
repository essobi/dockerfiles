FROM ubuntu:14.04  
ENV NODEJS_VERSION=0.12.3  
# Learn from google, but use taobao mirror and differeinstallnt version  
RUN apt-get update -y && \  
apt-get install --no-install-recommends -y -q \  
build-essential \  
ca-certificates \  
curl \  
git \  
python  
  
RUN mkdir /nodejs && \  
curl
http://npm.taobao.org/mirrors/node/latest/node-v${NODEJS_VERSION}-linux-x64.tar.gz
| tar xvzf - -C /nodejs --strip-components=1  
ENV PATH=$PATH:/nodejs/bin  
  

