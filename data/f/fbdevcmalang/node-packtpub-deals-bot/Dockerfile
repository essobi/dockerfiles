FROM node:7.4  
RUN npm install pm2 -g  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
  
COPY . /usr/src/app  
  
EXPOSE 8080  
CMD [ "pm2-docker", "index.js" ]  

