FROM selenium/standalone-chrome  
MAINTAINER Vohtr (https://vohtr.com)  
  
USER root  
  
# Install build tools  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
g++ \  
git \  
ssh \  
python \  
&& apt-get -y autoclean \  
&& rm -rf /var/lib/apt/lists/*  
  
# NVM environment variables  
ENV NVM_DIR "/usr/local/nvm"  
ENV NVM_VERSION 0.33.11  
ENV NODE_VERSION 8.11.1  
# Install NVM  
RUN mkdir -p $NVM_DIR \  
&& curl --silent -o-
https://raw.githubusercontent.com/creationix/nvm/v$NVM_VERSION/install.sh |
bash  
  
# Install NodeJS and NPM  
RUN /bin/bash -c 'source $NVM_DIR/nvm.sh; \  
nvm install $NODE_VERSION; \  
nvm alias default $NODE_VERSION; \  
nvm use default;'  
  
# Add node and npm to path so the commands are available  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# Install WebdriverIO & Chimp  
# --unsafe-perm -> https://github.com/nodejs/node-gyp/issues/454  
RUN npm install -g --unsafe-perm \  
chai \  
webdriverio \  
chimp  
  
# Install Meteor  
RUN curl https://install.meteor.com/ | sh  
  
USER seluser

