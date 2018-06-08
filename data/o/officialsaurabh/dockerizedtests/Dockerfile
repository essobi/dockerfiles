FROM node:carbon  
WORKDIR /usr/src/app  
COPY ./App/package*.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
CMD node app.js  
EXPOSE 8000  

