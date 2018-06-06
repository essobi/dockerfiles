FROM iromu/weplay-common:latest  
  
# Create app directory  
RUN mkdir -p /usr/src/app/compressor  
WORKDIR /usr/src/app/compressor  
  
COPY . .  
  
# Install app dependencies  
RUN yarn install  
RUN yarn link weplay-common  
RUN yarn  
  
# Setup environment  
ENV NODE_ENV production  
ENV DISCOVERY_URL "http://discovery:3080"  
ENV WEPLAY_REDIS_URI "redis:6379"  
ENV WEPLAY_LOGSTASH_URI "logstash:5001"  
# Run  
CMD ["yarn", "start"]  

