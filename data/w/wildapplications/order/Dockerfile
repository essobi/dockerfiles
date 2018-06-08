FROM node:boron  
  
# Create app directory  
RUN mkdir -p /usr/app  
WORKDIR /usr/app  
  
# Install app dependencies  
COPY package.json /usr/app  
RUN npm install  
  
# Bundle app source  
ADD src /usr/app/src  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

