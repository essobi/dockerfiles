# DOCKER-VERSION 1.0.0  
FROM withinboredom/consul-agent  
MAINTAINER Robert Landers <landers.robert@gmail.com>  
  
# Setup Node.js (Setup NodeSource Official PPA)  
# https://github.com/nodesource/docker-
node/blob/master/ubuntu/trusty/Dockerfile  
RUN curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get update && \  
apt-get install -y --force-yes apt-transport-https lsb-release python-all git
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
env NODE_VERSION 4.1.1  
env NPM_VERSION 3.3.3  
env NVM_SYMLINK_CURRENT "true"  
run touch /.profile && curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.25.4/install.sh |
NVM_DIR=/usr/local/nvm PROFILE=/.profile bash  
run . /.profile && nvm install $NODE_VERSION && nvm use $NODE_VERSION && nvm
alias default $NODE_VERSION  
run . /.profile && npm install -g npm && npm install -g forever  

