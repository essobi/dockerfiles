FROM node:4-alpine  
# Home directory for Node-RED application source code.  
RUN mkdir -p /usr/src/node-red /node  
WORKDIR /usr/src/node-red  
# package.json contains Node-RED NPM module and node dependencies  
COPY package.json /usr/src/node-red/  
RUN npm install  
  
RUN npm install -g node-inspector  
  
COPY 80-function.js 80-template.html 80-template.js /usr/src/node-
red/node_modules/node-red/nodes/core/core/  
  
# User configuration directory volume  
EXPOSE 1880  
# Environment variable holding file path for flows configuration  
ENV FLOWS=/flows.json  
  
ENV NODE_EXEC=node  
COPY /entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

