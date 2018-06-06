FROM keymetrics/pm2-docker-alpine:latest  
  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN npm install --production --silent  
  
CMD ["pm2-docker", "pm2.json"]  

