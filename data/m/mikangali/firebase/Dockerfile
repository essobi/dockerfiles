FROM node:6.13.0  
  
MAINTAINER Michael <mike@mikangali.com>  
  
ENV IONIC_VERSION=3.15.2 \  
CORDOVA_VERSION=6.4.0 \  
NPM_VERSION=3.10.10 \  
HEXO_CLI_VERSION=1.0.4 \  
FIREBASE_TOOL_VERSION=3.17.4  
  
# Instal npm tools  
RUN npm i -g --unsafe-perm cordova@${CORDOVA_VERSION} ionic@${IONIC_VERSION}
firebase-tools@${FIREBASE_TOOL_VERSION} hexo-cli@${HEXO_CLI_VERSION}  
  
WORKDIR "/app"  

