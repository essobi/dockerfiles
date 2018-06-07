FROM node:9  
  
RUN npm install --global signalhub@4.8.0  
  
ENV PORT 8080  
EXPOSE 8080  
  
CMD signalhub listen -p ${PORT}  

