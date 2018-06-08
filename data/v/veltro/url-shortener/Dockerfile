FROM iojs:latest  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
  
VOLUME /usr/src/app/data  
EXPOSE 3000  
CMD [ "npm", "start" ]  

