FROM node:6  
  
ENV NODE_ENV=production  
  
RUN mkdir -p /usr/src/app  
  
COPY server /usr/src/app/server  
COPY package.json /usr/src/app  
  
WORKDIR /usr/src/app  
  
RUN npm install  
  
EXPOSE 3000  
  
CMD node .  

