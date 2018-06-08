FROM node:8.1  
ENV MONGODB_URL $MONGODB_URL  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app  
RUN npm install  
  
COPY . /usr/src/app  
EXPOSE 3000  
CMD npm start app.js  

