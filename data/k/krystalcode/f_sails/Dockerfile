FROM krystalcode/f_nvm  
  
# Set the Node.js version to the latest available within Node.js version 6.  
ENV NODE_VERSION 6  
# Install the right Node.js version and set it as default.  
RUN . ${HOME}/.nvm/nvm.sh && \  
nvm install ${NODE_VERSION} && \  
printf '\n%s\n%s%s\n\n' '# Use default node version.' "nvm use "
${NODE_VERSION} >> ~/.bashrc && \  
  
# Install 'sails'.  
nvm use ${NODE_VERSION} && \  
npm install -g sails  
  
EXPOSE 1337  
# Run the application.  
CMD . ${HOME}/.nvm/nvm.sh && \  
nvm use ${NODE_VERSION} && \  
sails lift  

