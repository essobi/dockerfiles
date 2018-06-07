FROM node:boron  
  
ENV HOME /root  
ENV TW_TRACKER $HOME/tweetping/tracker-view  
  
WORKDIR $TW_TRACKER  
  
COPY ./package.json package.json  
  
RUN npm install --production  
  
COPY ./app/ ./app/  
COPY ./config/ ./config/  
COPY ./entrypoint-search.sh ./entrypoint.sh  
  
EXPOSE 3000  
ENTRYPOINT ["/root/tweetping/tracker-view/entrypoint.sh"]  

