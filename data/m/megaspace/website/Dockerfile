FROM node:5  
COPY . /app  
  
RUN cd /app; npm install; npm install -g coffee-script  
  
CMD ["coffee", "/app/src/app.coffee"]  

