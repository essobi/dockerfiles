FROM node:5.9.1  
# create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 3000  
CMD [ "npm", "start" ]  

