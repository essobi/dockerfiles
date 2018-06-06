FROM node:8-alpine  
COPY . /home/node/app/  
WORKDIR /home/node/app  
RUN npm install --production  
ENTRYPOINT NODE_ENV=production node index.js

