# We use Ubuntu 12.04 (precise) as our base image due to problems with Xvfb in  
# Docker on Ubuntu 14.04 (trusty)  
FROM ubuntu:precise  
MAINTAINER RedJack, LLC  
  
ENV NODE_VERSION stable  
ENV PATH /usr/local/bin:$PATH  
  
# Install build dependencies for Nave  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
build-essential \  
curl \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Nave  
RUN curl -f -o /usr/local/bin/nave
https://raw.githubusercontent.com/isaacs/nave/master/nave.sh  
RUN chmod a+x /usr/local/bin/nave  
  
# Build/install NodeJS  
RUN nave usemain $NODE_VERSION  

