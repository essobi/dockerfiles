FROM ubuntu:14.04  
MAINTAINER James Sharp <james@ortootech.com>  
  
# Build dependencies  
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty main universe' >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install --no-install-recommends -y -q curl && apt-get clean  
RUN apt-get install --no-install-recommends -y -q build-essential && apt-get
clean  
RUN apt-get install --no-install-recommends -y -q python2.7  
RUN ln -s /usr/bin/python2.7 /usr/bin/python  
  
# Install node  
RUN NODE_VER=0.10.35 && \  
NODE_FILE=node-v$NODE_VER-linux-x64.tar.gz && \  
curl -o /tmp/$NODE_FILE http://nodejs.org/dist/v$NODE_VER/$NODE_FILE && \  
cd /usr/local && tar --strip-components 1 -xzf /tmp/$NODE_FILE && \  
rm /tmp/$NODE_FILE  
  
# Install node-inspector  
RUN npm install -g node-inspector jasmine-node

