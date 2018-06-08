FROM node:6.1.0  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
RUN mkdir /data  
  
VOLUME /data  
EXPOSE 3000  
CMD [ "npm", "start" ]  

