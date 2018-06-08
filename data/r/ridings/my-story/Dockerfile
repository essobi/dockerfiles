FROM node:5.3.0  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
  
EXPOSE 8001:8001  
CMD ["node","/usr/src/app/app.js"]  

