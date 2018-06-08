FROM node:6.3-slim  
  
COPY services /app/services  
COPY package.json /app  
COPY dyson-server.js /app  
COPY dyson.json /app  
  
WORKDIR /app  
  
RUN npm install -g nodemon  
RUN npm install  
  
ENTRYPOINT nodemon .  

