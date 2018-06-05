FROM node:6.4.0  
ADD . /app  
  
WORKDIR /app  
RUN ["npm", "i"]  
  
EXPOSE 1234  
ENTRYPOINT ["node", "/app/index.js"]  

