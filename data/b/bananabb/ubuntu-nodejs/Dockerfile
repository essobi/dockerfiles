FROM bananabb/ubuntu-base:base.2.0.0  
MAINTAINER BananaBb  
  
# Install Node.js  
RUN sudo apt-get update \  
&& sudo apt-get install -y \  
nodejs \  
npm \  
build-essential \  
libssl-dev  
  
# Use `Node.js 6.0.0` by `NVM`(node.js version manager)  
ENV NVM_DIR $HOME/.nvm  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \  
&& [ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh" \  
&& [ -s "$NVM_DIR/bash_completion" ] && \\. "$NVM_DIR/bash_completion" \  
&& nvm install 6.0.0 \  
&& nvm alias default 6.0.0 \  
&& nvm use default  
  
# Install pm2  
RUN npm install pm2 -g  
  
# Create working DirectoryRUN /bin/bash -c "  
RUN mkdir -p /var/www/public  
WORKDIR /var/www/public  
  
EXPOSE 80 443  
CMD ["/bin/bash"]

