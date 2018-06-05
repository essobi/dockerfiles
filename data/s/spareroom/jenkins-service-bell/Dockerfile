FROM node:6.10.3-alpine  
  
ADD ./lib /app/lib  
ADD ./index.js /app/index.js  
ADD ./package.json /app/package.json  
  
WORKDIR /app  
  
RUN npm i --production  
  
ENTRYPOINT ["node", "."]  

