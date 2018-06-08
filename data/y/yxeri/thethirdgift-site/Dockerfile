FROM node:5.5.0  
EXPOSE 8888  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
  
CMD [ "npm", "start" ]  

