  
FROM wnameless/oracle-xe-11g  
  
MAINTAINER Mikael Lepistö <mikael.lepisto@vincit.com>  
  
# NVM install from http://stackoverflow.com/a/28390848/360060  
  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Set debconf to run non-interactively  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Install base dependencies  
RUN apt-get update && apt-get install -y -q --no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
git \  
libssl-dev \  
python \  
rsync \  
software-properties-common \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV NVM_DIR /usr/local/nvm  
ENV DEFAULT_NODE_VERSION 6  
  
# Install nvm with node and npm  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh |
bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install 4 \  
&& nvm install 5 \  
&& nvm install 6 \  
&& nvm install 7 \  
&& nvm alias default $DEFAULT_NODE_VERSION \  
&& nvm use default  

