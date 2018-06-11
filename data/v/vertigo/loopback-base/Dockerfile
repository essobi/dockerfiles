#  
# Base Loopback (over Node)  
#  
FROM node:9  
  
ARG NPM_REG  
  
# loopback cli tool  
RUN npm -g config set user root && \  
npm install -g loopback-cli $NPM_REG && \  
npm install -g nodemon $NPM_REG && \  
npm -g config set user nobody && \  
npm cache clear --force  
  
WORKDIR /usr/app  
  

