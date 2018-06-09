FROM node:0.10.38  
RUN apt-get update  
  
RUN mkdir -p /usr/src/app/swim  
WORKDIR /usr/src/app/swim  
COPY package.json /usr/src/app/swim/  
RUN npm install  
  
COPY . /usr/src/app/swim  
  
ENTRYPOINT ["npm", "start"]  
EXPOSE 8080  

