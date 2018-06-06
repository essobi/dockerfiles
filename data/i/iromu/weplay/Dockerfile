FROM iromu/weplay-common:latest  
  
# Create app directory  
RUN mkdir -p /usr/src/app/io  
WORKDIR /usr/src/app/io  
  
COPY . .  
  
# Install app dependencies  
RUN yarn install  
RUN yarn link weplay-common  
RUN yarn  
  
# Setup environment  
ENV NODE_ENV production  
ENV WEPLAY_PORT 8081  
ENV DISCOVERY_URL "http://discovery:3080"  
ENV WEPLAY_REDIS_URI "redis:6379"  
ENV WEPLAY_REDIS "redis://redis:6379"  
ENV WEPLAY_LOGSTASH_URI "logstash:5001"  
EXPOSE 8081  
# Run  
CMD [ "yarn", "start" ]  

