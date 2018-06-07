FROM node:boron  
  
# Create app directory  
RUN mkdir -p /var/www/app  
  
# Bundle app source  
COPY . /var/www/app  
WORKDIR /var/www/app/src  
RUN npm install  
  
EXPOSE 3000  
CMD [ "node", "server.js" ]

