FROM debian:jessie  
  
ENV NVM_DIR $HOME/.nvm  
  
ENV NODE_VERSION 7.9  
  
RUN apt-get update -yqq && apt-get -yqq install ca-certificates curl git lftp  
  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash &&
\  
\\. "$NVM_DIR/nvm.sh" && \  
nvm install $NODE_VERSION && \  
npm install -g yarn && \  
rm -rf /var/lib/apt/lists/*  

