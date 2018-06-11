FROM node:8  
# Create app directory  
RUN mkdir -p /usr/src/DataIntegrationManagement  
WORKDIR /usr/src/DataIntegrationManagement  
  
# Bundle app source  
COPY . /usr/src/DataIntegrationManagement  
  
# Install app dependencies  
RUN WITH_SASL=0 npm install  
  
CMD [ "node", "index.js"]  

