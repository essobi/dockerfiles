FROM node:7.1.0  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY src/package.json /usr/src/app/  
RUN npm install  
  
COPY src/api /usr/src/app/api  
COPY src/index.js /usr/src/app  
COPY src/controllers /usr/src/app/controllers  
  
EXPOSE 8081  
CMD [ "npm", "start" ]  

