FROM node:5.12.0  
MAINTAINER tim@emmaeins.io  
  
ADD . /app  
  
WORKDIR /app  
  
RUN npm install  
RUN node_modules/.bin/gulp  
  
CMD ["npm", "start"]

