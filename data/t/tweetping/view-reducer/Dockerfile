FROM node:boron  
  
ENV HOME /root  
ENV TW_TRACKER $HOME/tweetping/tracker-view  
  
WORKDIR $TW_TRACKER  
  
COPY ./package.json package.json  
  
RUN npm install --production  
  
COPY ./app/ ./app/  
COPY ./config/ ./config/  
  
CMD ["node", "app/reducer/server.js"]  

