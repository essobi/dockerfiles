FROM node:4-slim  
  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN cd /usr/src/app && npm install  
COPY . /usr/src/app  
  
CMD [ "npm", "start" ]  
  
EXPOSE 8080  

