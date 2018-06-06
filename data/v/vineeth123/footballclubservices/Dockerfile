FROM node  
  
WORKDIR /home/saudi-fc-service  
  
ADD package.json /home/saudi-fc-service/package.json  
RUN npm install  
  
ADD . /home/saudi-fc-service  
  
EXPOSE 3000  
CMD ["node", "server.js"]

