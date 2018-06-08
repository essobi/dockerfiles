FROM node:alpine  
MAINTAINER mckenzie <wsmckenz@cartewright.com>  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
  
# Install app dependencies  
RUN npm install -g mocha typescript typings  
RUN npm install  
RUN typings install  
RUN tsc -p src  
  
# Expose the web and the websocket ports.  
EXPOSE 8081  
#  
CMD [ "node", "dist/bin/server", "--storeModule", "null" ]  

