FROM ubuntu:14.04  
MAINTAINER Jesse Panganiban <jesse.panganiban@infoshiftinc.com>  
  
ENV NODE_VERSION v0.10.29  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y build-essential python wget  
  
# Fetch  
RUN wget http://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.gz -O
/tmp/node-${NODE_VERSION}.tar.gz  
  
# Install  
RUN cd /tmp && tar -xf node-${NODE_VERSION}.tar.gz && \  
cd /tmp/node-${NODE_VERSION} && \  
./configure && \  
make && \  
make install  
  
# Cleanup  
RUN rm -rf /tmp/node-${NODE_VERSION} && \  
rm -rf /tmp/node-${NODE_VERSION}.tar.gz  

