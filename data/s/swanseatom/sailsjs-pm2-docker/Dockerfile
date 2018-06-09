FROM node:8  
MAINTAINER Tom Riley <tom@tom-riley.tech>  
RUN npm install -g sails pm2  
VOLUME [ "/app" ]  
EXPOSE 1337  
WORKDIR /app  
CMD npm install && pm2-docker start app.js  

