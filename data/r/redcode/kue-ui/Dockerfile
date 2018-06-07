FROM node:8-alpine  
  
WORKDIR /src  
  
COPY package.json /src/package.json  
RUN npm install --production  
  
COPY . /src  
  
CMD ["node", "/src/index.js"]  

