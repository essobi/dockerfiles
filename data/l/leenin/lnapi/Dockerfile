FROM node:8.2.1-alpine  
  
RUN mkdir /app  
  
WORKDIR /app  
  
ADD . /app/  
  
RUN npm install --production  
  
ONBUILD ADD apib /app/src/apib  
  
EXPOSE 8000  
CMD ["npm", "start"]  

