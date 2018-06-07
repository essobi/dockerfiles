FROM node:carbon  
  
RUN git clone https://448ab958c5599ae4fca91a775ddd27b51db36d6d:x-oauth-
basic@github.com/JackFay/AwesomeProjectBackend /app/  
  
WORKDIR /app  
  
RUN npm install  
  
RUN mv ./setup/keras-js/index.js ./node_modules/keras-js/lib/index.js  
  
EXPOSE 8080  
CMD ["npm", "run", "dev"]  

