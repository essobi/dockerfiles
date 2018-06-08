FROM node:carbon  
  
WORKDIR /Flashfood  
  
ADD . /Flashfood  
  
RUN npm install express  
RUN npm install request  
RUN npm install apiai  
RUN npm install bluebird  
RUN npm install mocha  
RUN npm install chai  
  
EXPOSE 5000  
ENV NAME node-sever  
  
CMD ["node","Flashbot.js"]  

