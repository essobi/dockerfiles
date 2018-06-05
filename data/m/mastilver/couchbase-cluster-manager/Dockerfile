FROM node:6  
MAINTAINER Thomas Sileghem <th.sileghem@gmail.com>  
  
COPY ./manager.js ./getNextState.js ./package.json ./  
  
RUN npm install --production  
  
ENTRYPOINT ["node", "./manager.js"]  

