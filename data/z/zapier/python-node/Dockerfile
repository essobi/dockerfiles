FROM zapier/python:2.7  
  
# Node.js  
  
RUN apt-get update && apt-get install -y curl gnupg git && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs && \  
node --version  
  
# Yarn  
  
RUN npm install --global yarn && \  
yarn --version  

