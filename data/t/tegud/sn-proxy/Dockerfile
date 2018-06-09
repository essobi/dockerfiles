FROM node:8.9  
CMD mkdir /app  
ADD ./index.js /app/index.js  
ADD ./package.json /app/package.json  
ADD ./lib /app/lib  
  
WORKDIR /app  
  
RUN npm install --production  
  
EXPOSE 3000  
ENTRYPOINT ["node", "index"]  

