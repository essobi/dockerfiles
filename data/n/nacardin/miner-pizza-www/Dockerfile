FROM node:8.1-alpine  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD . /usr/src/app/  
RUN rm -fr node_modules  
RUN npm install  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

