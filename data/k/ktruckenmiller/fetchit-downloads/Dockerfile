FROM node:8.1.3  
RUN mkdir /build  
COPY package.json /build  
WORKDIR /build  
RUN npm install  
COPY . /build  
EXPOSE 3000  
CMD node app.js  

