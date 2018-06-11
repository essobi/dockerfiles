FROM node:argon  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN npm install && npm run build  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

