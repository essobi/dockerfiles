FROM node:7.8-slim  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# use nodemon for development  
RUN npm install --global nodemon eslint  
  
# use cached layer for node modules  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /usr/src && cp -a /tmp/node_modules /usr/src/  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

