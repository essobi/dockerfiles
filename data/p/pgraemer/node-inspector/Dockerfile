FROM node:latest  
RUN mkdir -p /opt/node-inspector  
WORKDIR /opt/node-inspector  
RUN npm install node-inspector  
VOLUME /opt/node-inspector  
ENTRYPOINT ["node_modules/.bin/node-inspector"]  

