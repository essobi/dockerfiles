FROM node:argon  
  
ENV HOME /root  
ENV TW_TRACKER $HOME/tweetping/event-handlers  
  
WORKDIR $TW_TRACKER  
  
COPY ./package.json .  
  
RUN npm install --production  
  
COPY ./app/ ./app/  
COPY ./config/ ./config/  
  
CMD ["node", "app/eventHandlersServer.js"]  

