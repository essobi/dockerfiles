FROM node:7-alpine  
  
RUN mkdir /app  
  
ADD ./ /app  
  
WORKDIR /app  
  
RUN npm i  
  
EXPOSE 3000  
CMD node index.js

