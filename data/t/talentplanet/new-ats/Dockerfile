FROM node:8  
WORKDIR /app  
  
ADD . /app  
  
RUN npm i  
  
##RUN npm run prod  
EXPOSE 3000  
ENTRYPOINT ["node", "server/server.js"]  

