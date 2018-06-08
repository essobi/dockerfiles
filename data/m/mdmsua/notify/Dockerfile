FROM node:slim  
MAINTAINER Dmytro Morozov "mdmsua@icloud.com"  
WORKDIR /var/www  
ADD index.js package.json /var/www/  
  
ENV NODE_ENV=production  
EXPOSE 80  
RUN npm i  
  
ENTRYPOINT ["npm", "start"]

