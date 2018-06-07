# Author  
# Pedro Silva  
FROM node:7.10-alpine  
MAINTAINER Pedro Silva  
  
# Default port  
EXPOSE 3000  
# Copy code and update configuration  
COPY . /home/ws-router/  
WORKDIR /home/ws-router/  
RUN npm install  
CMD node app.js  

