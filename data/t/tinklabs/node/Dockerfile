FROM node:6.9.5-alpine  
  
RUN apk add --no-cache bash tzdata  
RUN npm install pm2 -g  
RUN pm2 install pm2-logrotate  
# RUN pm2 set pm2-logrotate:max_size 100M  
# RUN pm2 set pm2-logrotate:retain 5  
# RUN pm2 set pm2-logrotate:compress true  
WORKDIR /app  
  
CMD ['pm2-docker start /app/pm2.config.js --node-args="--max-old-space-
size=1024"']  

