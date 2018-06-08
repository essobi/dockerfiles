FROM kdelfour/cloud9-docker  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.30.1/install.sh |
NVM_DIR="/nvm" bash  
RUN bash -c "source /nvm/nvm.sh && nvm install 4.2.4 && nvm alias default
v4.2.4"  
RUN bash -c "export USER=root && export HOME=/tmp && source /nvm/nvm.sh && nvm
use default && npm install -g mojoio"  
EXPOSE 80  

