# Dockerfile for test branch  
# Built command: docker build -t testserver .  
# Run command: docker run -p 8100:8100 -it testserver  
# Application run this adress: http://138.197.157.84:8100  
FROM ubuntu:16.04  
MAINTAINER Guillaume Piché Francis Poirier Remykia Hellal version: 0.1  
# Update ubuntu, install curl, install git, install clean and install vim  
RUN apt-get update && \  
apt-get install -y curl git wget vim python build-essential &&\  
apt-get clean  
  
# Configure Github  
RUN git config --global user.email "gpiche1@yahoo.ca" &&\  
git config --global user.name "gpiche"  
  
# Install Nnode version manager  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 8.6.0  
# Install nvm with node and npm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.5/install.sh | bash \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
RUN ls -al $NVM_DIR/versions/node/v$NODE_VERSION/bin  
  
# confirm installation  
RUN node -v  
RUN npm -v  
  
# Install Ionic2  
RUN npm install -g cordova ionic  
  
#Install chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main'
| tee /etc/apt/sources.list.d/google-chrome.list  
RUN apt-get update  
RUN apt-get install -y google-chrome-stable  
  
# Project  
RUN rm -rf Projet-Vaolo  
RUN git clone https://github.com/RemikyaHellal/Projet-Vaolo.git  
  
WORKDIR /Projet-Vaolo  
  
# Branch of tests  
RUN git checkout test  
  
#Install Ionic Projet/Run tests  
RUN npm install  
  
EXPOSE 8100 35729  
ARG REPETER=unknown  
RUN echo "#!/bin/bash" >> test.sh  
RUN echo "git pull" >> test.sh  
RUN echo "npm run test" >> test.sh  
RUN chmod u+x test.sh  
  
ENTRYPOINT ["./test.sh"]  
  

