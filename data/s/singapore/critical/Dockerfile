FROM node:5.11  
# Create app directory  
RUN mkdir -p /usr/src/critical  
WORKDIR /usr/src/critical  
  
# Bundle app source  
COPY . /usr/src/critical  
  
# Install app dependencies  
RUN npm -q install && npm cache clean  
  
CMD [ "node", "index.js" ]  

