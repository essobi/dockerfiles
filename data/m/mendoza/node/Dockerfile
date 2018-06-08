FROM ubuntu  
MAINTAINER Alberto Mendoza <mendozaene@gmail.com>  
  
# Required packages  
RUN apt-get update && apt-get install -y build-essential libssl-dev curl man  
  
# Download source for install node v0.16.1  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.16.1/install.sh |
sh  
ENV NVM_DIR=/root/.nvm  
ENV INSTALL_NODE_VERSION=v4.4.5  
# Install node version and set default  
RUN . $HOME/.nvm/nvm.sh && \  
nvm install $INSTALL_NODE_VERSION && \  
nvm alias default $INSTALL_NODE_VERSION && \  
nvm use default && \  
npm update -g  
# Node v4.4.5 ready and npm updated  

