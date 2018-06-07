# Use an official Google Cloud SDK as a parent image  
FROM google/cloud-sdk  
  
# Install NVM Node.js version manager and Node.js 6.11.2  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.4/install.sh | bash \  
&& export NVM_DIR="$HOME/.nvm" \  
&& [ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh" \  
&& nvm install 6.11.2  
  
ENTRYPOINT ["/bin/bash"]  

