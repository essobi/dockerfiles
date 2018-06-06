FROM node:latest  
RUN npm install pm2 -g  
COPY . .  
RUN npm i --no-save --production  
USER node  
CMD [ "pm2-docker", "index.js" ]  

