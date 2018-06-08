FROM node:alpine  
  
WORKDIR /src  
  
COPY package.json /src/package.json  
RUN npm install  
COPY . /src  
  
VOLUME $WORKING_DIR/node_modules  
CMD [ "npm", "start" ]  

