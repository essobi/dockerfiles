FROM node:8.1.0-alpine  
  
# Create app directory  
RUN mkdir -p /usr/src/webapp  
WORKDIR /usr/src/webapp  
  
# Install app dependencies  
RUN npm install -g typescript  
RUN npm install -g webpack  
  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN cp -a /tmp/node_modules /usr/src/webapp  
  
# Bundle app source  
ADD . /usr/src/webapp  
RUN npm run build  
  
EXPOSE 3000  
CMD [ "npm", "run", "server" ]  

