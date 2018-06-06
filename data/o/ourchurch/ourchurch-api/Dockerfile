FROM node:4  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install --production  
COPY . /usr/src/app  
  
EXPOSE 8080  
ENTRYPOINT ["node", "ourchurch.js"]  

