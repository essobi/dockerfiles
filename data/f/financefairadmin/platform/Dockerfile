FROM node:latest  
  
MAINTAINER Shane Gray <shane.joseph.gray@gmail.com>  
  
RUN npm install -g gulp  
  
WORKDIR /home/api  
COPY . /home/api  
  
RUN npm install  
RUN gulp build-client  
  
EXPOSE 3000  
CMD ["node", "server.js"]  

