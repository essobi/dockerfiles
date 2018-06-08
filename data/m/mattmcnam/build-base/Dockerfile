FROM ubuntu:16.04  
MAINTAINER Matthew McNamara <mattmcnam@gmail.com>  
  
# Replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update && \  
apt-get install -y python python-pip build-essential curl && \  
pip install --upgrade b2 && \  
curl -o\- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh
| bash && \  
export NVM_DIR="$HOME/.nvm" && . "$NVM_DIR/nvm.sh" && \  
nvm install 6 && \  
npm install -g npm@latest  
COPY .bashrc /root/  

