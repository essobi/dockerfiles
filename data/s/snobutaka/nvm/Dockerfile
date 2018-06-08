FROM centos:7  
SHELL [ "/bin/bash", "-c" ]  
  
# Install [nvm](https://github.com/creationix/nvm).  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash  
  
# Install Node.js v8.10.0 and upgrade npm from 5.6.1 to 5.7.1.  
ENV NVM_DIR="/root/.nvm"  
RUN . "$NVM_DIR/nvm.sh" && \  
. "$NVM_DIR/bash_completion" && \  
nvm install v8.10.0 && \  
nvm alias default v8.10.0 && \  
npm install npm@5.7.1 -g  
  
COPY entrypoint.sh /  
ENTRYPOINT [ "/entrypoint.sh" ]  

