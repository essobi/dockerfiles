FROM node:7.2.0-alpine  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app  
RUN npm install  
COPY . /usr/src/app  
RUN npm run build  
  
EXPOSE 5000  
CMD [ "npm", "run", "cluster" ]  

