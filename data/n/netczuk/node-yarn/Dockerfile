FROM node:boron  
  
MAINTAINER Tomasz Netczuk  
  
RUN npm i -g yarn@0.21.3  
RUN npm cache clean  
# fix for: .roadrunner.json error https://github.com/yarnpkg/yarn/issues/1724  
RUN mkdir -p /root/.cache/yarn/  
RUN yarn --version  

