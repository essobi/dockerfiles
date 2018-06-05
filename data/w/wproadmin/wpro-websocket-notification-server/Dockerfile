FROM node:4.3.2  
COPY ./package.json /app/package.json  
COPY ./npm-shrinkwrap.json /app/npm-shrinkwrap.json  
  
WORKDIR /app/  
RUN npm install  
  
COPY ./server.js /app/server.js  
  
EXPOSE 8080  
ENTRYPOINT ["node", "/app/server.js"]  

