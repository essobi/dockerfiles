FROM node:8.11  
RUN mkdir /app  
  
COPY package.json /app/package.json  
COPY npm-shrinkwrap.json /app/npm-shrinkwrap.json  
COPY Gruntfile.js /app/Gruntfile.js  
COPY server.js /app/server.js  
COPY src /app/src  
  
WORKDIR /app  
RUN npm install && npm run build:dist; rm -rf /app/src  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

