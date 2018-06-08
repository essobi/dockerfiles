FROM node:8.7.0-alpine  
  
COPY package.json ./  
  
RUN npm install -g --quiet pkg && npm install --quiet --production  
  
ADD /src ./src  
  
RUN pkg -c package.json --output ./release/drone-consul src/index.js  
  
RUN rm -rf ./src node_modules package.json package-lock.json  
  
CMD ["/release/drone-consul"]  

