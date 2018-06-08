FROM debian:jessie  
  
ENV NVM_VERSION v0.13.1  
### Create development user ###  
RUN useradd -m sailor -s /bin/bash  
  
### Install c++ compiler ###  
RUN apt-get update && \  
apt-get install -y build-essential libssl-dev curl  
  
### Change user ###  
USER sailor  
  
### Fetch nvm package ###  
RUN curl
https://raw.githubusercontent.com/creationix/nvm/$NVM_VERSION/install.sh |
bash  
  
### Install node default version ###  
ENV NVM_DIR /home/sailor/.nvm  
ENV NODE_VERSION 6.9.1  
RUN . $NVM_DIR/nvm.sh && \  
nvm install v$NODE_VERSION && \  
nvm alias default $NODE_VERSION && \  
nvm use default  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
  
ENV PATH $NVM_DIR/v$NODE_VERSION/bin:$NVM_DIR:$PATH  
  
WORKDIR /home/sailor/  
  
CMD tail -f /var/log/lastlog  

