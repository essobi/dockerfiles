FROM node:6  
RUN mkdir /replicator/  
WORKDIR /replicator/  
  
COPY package.json package.json  
RUN npm install  
COPY index.js index.js  
  
CMD node index.js  

