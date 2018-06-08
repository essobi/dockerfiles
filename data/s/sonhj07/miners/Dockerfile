FROM node:7  
WORKDIR /binb_webserver  
COPY package.json /binb_webserver  
RUN npm install  
COPY . /binb_webserver  
CMD node index.js  
EXPOSE 8080  

