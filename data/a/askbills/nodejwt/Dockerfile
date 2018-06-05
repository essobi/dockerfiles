FROM node:latest  
  
# Create app directory  
RUN mkdir -p /usr/src/nodejwt  
WORKDIR /usr/src/nodejwt  
  
# Monitor for any changes in your node.js application and automatically
restart the server  
RUN npm install nodemon -g  
  
# Install app dependencies  
COPY package.json /usr/src/nodejwt/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/nodejwt  
  
EXPOSE 3000  
CMD ["npm", "start"]  

