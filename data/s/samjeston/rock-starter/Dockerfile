FROM node:6.3.1  
RUN apt-get update  
RUN apt-get install -y sox libsox-fmt-mp3  
  
RUN npm i -g pm2  
COPY . /app  
WORKDIR /app  
  
RUN npm install  
EXPOSE 3000  
CMD pm2 start ./index.js --no-daemon  

