FROM node:0.12.7  
MAINTAINER David Li <legendarilylwq@gmail.com>  
  
RUN npm install express body-parser request dockerode  
  
VOLUME ["/usr/src/app"]  
  
EXPOSE 4000  
WORKDIR /usr/src/app  
  
CMD ["node", "app.js"]  

