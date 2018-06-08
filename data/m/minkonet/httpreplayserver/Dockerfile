FROM node:4.5.0  
WORKDIR /tmp  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-
amd64-v0.2.0.tar.gz  
RUN tar -C /usr/local/bin -xvzf dockerize-linux-amd64-v0.2.0.tar.gz  
  
RUN mkdir -p /opt/swing/shared/logs/  
  
WORKDIR /opt/swing/sources/unrealhttpreplayserver  
COPY . .  
  
COPY package.json package.json  
RUN npm install  
  
EXPOSE 3000  
CMD dockerize -template confs/conf-DOCKER.js:confs/conf.js -timeout 60s npm
start  

