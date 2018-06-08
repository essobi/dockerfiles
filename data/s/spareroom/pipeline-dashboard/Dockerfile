FROM node:8.0.0-alpine  
  
ADD ./lib /app/lib  
ADD ./static /app/static  
ADD ./views /app/views  
ADD ./index.js /app/index.js  
ADD ./package.json /app/package.json  
  
WORKDIR /app  
  
RUN npm i --production  
  
ENTRYPOINT ["node", "."]  

