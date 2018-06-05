FROM node:8.9.0  
# Create app directory  
ADD . /usr/src/app  
  
WORKDIR /usr/src/app  
  
RUN npm install --production  
  
EXPOSE 3000  
CMD [ "npm", "start"]  

