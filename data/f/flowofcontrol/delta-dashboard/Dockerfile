FROM node  
  
MAINTAINER Langens Jonathan <flowofcontrol@gmail.com>  
  
ADD server.js /app/server.js  
  
ADD package.json /app/package.json  
  
WORKDIR /app  
  
RUN npm install  
  
EXPOSE 3000  
CMD ["npm", "run", "start"]  

