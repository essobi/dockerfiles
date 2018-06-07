FROM dreipunktnull/docker-php-base:7.1  
ENV NVM_DIR $HOME/.nvm  
  
ENV NODE_VERSION 8.4  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash &&
\  
\\. "$NVM_DIR/nvm.sh" && \  
nvm install $NODE_VERSION && \  
npm install -g yarn  
  
# Expand path to opt  
ENV PATH /opt/bin:$PATH  

