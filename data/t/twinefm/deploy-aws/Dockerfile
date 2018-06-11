FROM ubuntu:14.04  
MAINTAINER Twine  
  
# Replace shell with bash so we can source files  
RUN rm /bin/sh \  
&& ln -s /bin/bash /bin/sh  
  
# Set debconf to run non-interactively  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Install base dependencies  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
libssl-dev \  
libfontconfig \  
build-essential \  
wget \  
git-core \  
python-pip \  
jq \  
curl  
  
# Install aws cli  
RUN pip install awscli  
  
# Install nvm with node and npm  
ARG NVM_DIR=/usr/local/nvm  
ARG NVM_VERSION=0.33.2  
ARG NODE_VERSION=8.1.0  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v$NVM_VERSION/install.sh |
bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm use $NODE_VERSION \  
&& n=$(which node) \  
&& n=${n%/bin/node} \  
&& chmod -R 755 $n/bin/* \  
&& cp -r $n/{bin,lib,share} /usr/local \  
&& nvm unload \  
&& rm -rf $NVM_DIR  
  
# Cleanup  
RUN apt-get clean \  
&& rm -rf ~/* /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& history -c  

