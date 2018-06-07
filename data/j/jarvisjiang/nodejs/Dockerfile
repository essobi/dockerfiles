FROM fedora  
MAINTAINER JarvisJiang <jiang115jie@gmail.com>  
  
ENV NODE_VERSION 0.11.14  
  
RUN \  
yum update -y \  
&& yum install -y wget gcc-c++ which make git \  
&& yum -y clean all \  
&& mkdir -p ~/node \  
&& cd ~/node \  
&& wget http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.gz \  
&& tar -xzvf node-v$NODE_VERSION.tar.gz \  
&& cd node-v$NODE_VERSION \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf ~/node

