FROM node:6.9.4-alpine  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ENV NODE_ENV production  
  
COPY package.json /usr/src/app/  
RUN npm install --quiet && npm cache clean --quiet  
COPY server.js /usr/src/app/  
  
EXPOSE 3000  
CMD [ "npm", "start" ]  

