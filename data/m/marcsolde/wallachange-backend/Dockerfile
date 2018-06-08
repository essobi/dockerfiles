FROM node:7-alpine  
  
WORKDIR /app  
COPY package.json /app  
RUN npm install  
RUN npm install -g pm2  
COPY . /app  
VOLUME /root/uploads/profile:/app/uploads/profile  
VOLUME /root/uploads/elements:/app/uploads/elements  
CMD ["pm2-docker" ,"server.js"]  

