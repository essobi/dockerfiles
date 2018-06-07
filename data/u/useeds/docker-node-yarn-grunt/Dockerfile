FROM node:8.7  
  
MAINTAINER Christian Dornbusch <christian.dornbusch@useeds.de>  
  
# Global install yarn package manager and grunt  
RUN apt-get update && apt-get install -y curl apt-transport-https && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn && \  
npm install --global grunt-cli && \  
apt-get install -y ruby ruby2.1-dev ruby-compass && \  
gem install compass  
  
WORKDIR /workspace  

