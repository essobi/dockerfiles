FROM node:argon  
  
# Create app directory  
RUN mkdir -p /usr/src/raml  
RUN mkdir -p /usr/src/app  
RUN mkdir -p /usr/src/app/mocker-server  
  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
  
COPY ./mocker-server /usr/src/app/mocker-server  
  
EXPOSE 3030  
CMD [ "npm", "start" ]  

