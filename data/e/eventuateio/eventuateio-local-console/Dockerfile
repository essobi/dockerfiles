FROM node:boron  
WORKDIR /app  
RUN curl --location https://github.com/eventuate-local/eventuate-
local/archive/console_prerelease.tar.gz | tar xzf -  
WORKDIR /app/eventuate-local-console_prerelease/eventuate-local-
console/eventuate-local-console-client  
RUN npm install --no-optional && npm install -g webpack && npm run build  
WORKDIR /app/eventuate-local-console_prerelease/eventuate-local-
console/eventuate-local-console-server  
RUN npm install --no-optional && npm run static && npm run build  
CMD node dist/index.js  

