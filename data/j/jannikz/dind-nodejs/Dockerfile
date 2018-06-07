FROM gitlab/dind  
  
MAINTAINER Jannik Zinkl <jz@trieb.work>  
  
RUN apt-get update && \  
apt-get install -y build-essential libfontconfig zip git apt-transport-https
ca-certificates curl openssl software-properties-common && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs && \  
npm install grunt -g && \  
npm install grunt-cli -g && \  
npm install findup-sync resolve nopt -g && \  
node --version && \  
npm --version && \  
apt-get autoremove -y  

