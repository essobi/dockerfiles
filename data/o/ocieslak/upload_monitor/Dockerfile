FROM node  
  
RUN mkdir /app  
WORKDIR /app  
ADD . /app  
  
RUN npm install  
  
RUN chmod -R 777 .  
  
CMD ["node", "/app/monitor.js"]

