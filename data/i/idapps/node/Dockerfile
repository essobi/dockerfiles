FROM idapps/ubuntu:latest  
  
MAINTAINER Javier Fonseca <idapps.ve@gmail.com>  
  
# Install NVM  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash  
  
ENV NVM_DIR /root/.nvm  
ENV NODE_VERSION 8.1.0  
RUN bash -c "source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default \  
&& ln /root/.nvm/versions/node/v8.1.0/bin/node /usr/bin/node \  
&& ln /root/.nvm/versions/node/v8.1.0/bin/npm /usr/bin/npm \  
&& npm install -g forever"  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
RUN node -v  
RUN npm -v  

