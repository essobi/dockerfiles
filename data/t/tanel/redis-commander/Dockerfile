FROM node:4-alpine  
  
RUN npm -g install redis-commander && rm -rf /root/.npm  
  
ENTRYPOINT ["redis-commander"]

