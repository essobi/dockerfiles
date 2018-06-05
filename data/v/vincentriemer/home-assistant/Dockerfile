FROM homeassistant/home-assistant  
  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# make sure apt is up to date  
RUN apt-get update --fix-missing  
RUN apt-get install -y curl  
RUN apt-get install -y build-essential libssl-dev libnss-mdns libavahi-compat-
libdnssd-dev samba-common wakeonlan telnet nmap  
  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 8.1.2  
# Install nvm with node and npm  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.30.1/install.sh |
bash \  
&& source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default \  
&& npm install -g ps4-waker  
  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  

