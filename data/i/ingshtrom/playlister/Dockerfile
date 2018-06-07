FROM keymetrics/pm2:8-alpine  
  
WORKDIR /opt/app  
COPY package*.json yarn.lock ./  
  
ENV NODE_ENV=production  
RUN yarn install  
  
COPY . .  
  
EXPOSE 3001  
CMD [ 'pm2-runtime', './bin/www' ]  

