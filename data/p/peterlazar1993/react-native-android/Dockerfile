FROM beevelop/android:latest  
  
# use bash instead of sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update -y && \  
apt-get install -y curl && \  
apt-get install -y git && \  
apt-get install -y build-essential&& \  
apt-get install -y libssl-dev && \  
apt-get install -y python python-dev python-distribute python-pip && \  
apt-get install -y ruby  
  
# set node build variables  
ENV NVM_DIR /usr/local/.nvm  
ENV NODE_VERSION 5.2.0  
# Install NVM  
RUN git clone https://github.com/creationix/nvm.git $NVM_DIR && \  
cd $NVM_DIR && \  
git checkout `git describe --abbrev=0 --tags`  
  
# Install default version of Node.js  
RUN source $NVM_DIR/nvm.sh && \  
nvm install $NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
nvm use default  
  
# source nvm to shell  
RUN echo "source ${NVM_DIR}/nvm.sh" > $HOME/.bashrc && \  
source $HOME/.bashrc  
  
# Set node environment variables  
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# install react-native-cli  
RUN npm install -g react-native-cli  
  
RUN which android  
RUN which adb  
RUN node --version  
RUN npm --version  
  
# Clean up  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get autoremove -y && \  
apt-get clean  

