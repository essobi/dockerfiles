FROM node:6  
COPY package.json package.json  
RUN npm install --production  
  
COPY client.js client.js  
COPY expressServer.js expressServer.js  
  
COPY webpack.config.production.js webpack.config.production.js  
COPY server/ForwarderService.js server/ForwarderService.js  
COPY public public  
COPY routes.js routes.js  
  
COPY src src  
RUN npm run build  
RUN rm -rf src  
  
COPY config/config.production.js config/config.production.js  
CMD npm run start  
  
EXPOSE 3000  

