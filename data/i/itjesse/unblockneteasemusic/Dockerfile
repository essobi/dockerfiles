FROM node:8.2.1-alpine  
  
ENV NODE_ENV production  
ENV VERSION 2.5.5  
RUN npm install unblock-netease-music@${VERSION} -g && npm cache clean --force  
  
EXPOSE 8123  
ENTRYPOINT ["unblockneteasemusic"]  
CMD ["-h"]  

