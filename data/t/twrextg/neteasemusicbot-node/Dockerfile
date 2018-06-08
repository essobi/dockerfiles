FROM node:alpine  
  
ENV LANG zh-TW  
ENV ADMIN_TELEGRAM_ID YOUR_TELEGRAM_ID  
ENV TOKEN BOT_TOKEN  
ENV LOG_CHANNEL_ID LOG_CHANNEL_ID  
ENV API_HOST https://api.example.com  
ENV API /api  
ENV DEFAULT_BITRATE 320  
ENV DOCKER true  
ENV CACHE false  
ENV REDIS_HOST YOUR_REDIS_HOST  
ENV REDIS_PORT 6379  
ADD app.js /bot/app.js  
ADD package.json /bot/package.json  
ADD langs/*.json /bot/langs/  
  
WORKDIR /bot  
  
RUN npm install ./  
  
CMD ["node", "./app.js"]

