FROM ubuntu:xenial  
MAINTAINER Tom Riley <tom@riley-johns.com>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update && apt-get -y install curl apt-transport-https ca-
certificates git  
  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 8.9.4  
ENV NVM_VERSION 0.33.6  
# Install nvm with node and npm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v$NVM_VERSION/install.sh |
bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
# Add node and npm to path so the commands are available  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# Install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y yarn  
  
# Install pm2  
RUN yarn global add pm2  

