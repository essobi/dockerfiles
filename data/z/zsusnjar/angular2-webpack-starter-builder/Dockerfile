# Builds a Docker image  
# see https://bitbucket.org/zarkosusnjar/angular-webpack-builder for current
version  
FROM node:latest  
  
# Install global npm dependencies  
RUN npm install --global typescript webpack webpack-dev-server karma-cli
protractor  
RUN webdriver-manager update  
  
# Make application directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Copy package file to working directory  
ADD npm-shrinkwrap.json /usr/src/app/npm-shrinkwrap.json  
ADD package.json /usr/src/app/package.json  
  
# Install dependencies  
RUN npm install && npm cache clear  
  
# Make a backup od modules  
RUN mkdir -p /usr/src/packages  
RUN cp -a /usr/src/app/node_modules /usr/src/packages/node_modules  
RUN rm -rf /usr/src/app/node_modules  

