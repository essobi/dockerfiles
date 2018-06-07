FROM node:7.5.0  
ENV CLIENT_DIR /usr/src/client  
  
RUN npm install --global @angular/cli && npm install --global typings  
  
RUN mkdir $CLIENT_DIR  
WORKDIR $CLIENT_DIR  
COPY package.json $CLIENT_DIR/package.json  
COPY typings.json $CLIENT_DIR/typings.json  
COPY . $CLIENT_DIR  
RUN npm install && typings install  
RUN ng build -prod  

