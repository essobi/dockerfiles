FROM debian:jessie  
MAINTAINER Josh Finnie <josh@jfin.us>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y git \  
curl \  
build-essential \  
libssl-dev  
  
ENV NVM_DIR /usr/local/.nvm  
ENV NODE_VERSION 4.1.2  
# Install nvm  
RUN git clone https://github.com/creationix/nvm.git $NVM_DIR && \  
cd $NVM_DIR && \  
git checkout `git describe --abbrev=0 --tags`  
  
# Install default version of Node.js  
RUN source $NVM_DIR/nvm.sh && \  
nvm install $NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
nvm use default  
  
# Add nvm.sh to .bashrc for startup...  
RUN echo "source ${NVM_DIR}/nvm.sh" > $HOME/.bashrc && \  
source $HOME/.bashrc  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/v$NODE_VERSION/bin:$PATH  

