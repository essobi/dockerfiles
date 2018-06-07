FROM jkilbride/node-npm-alpine:latest  
  
RUN mkdir -p /src  
  
ADD ./src /src  
  
WORKDIR /src  
  
RUN npm install -g node-red node-red-contrib-amqp node-red-contrib-bigsplitter  
RUN npm install -g node-red-contrib-jwt node-red-contrib-bcrypt node-red-
contrib-redis  
RUN npm install -g node-red-contrib-mongodb2 node-red-contrib-elasticsearch3
node-red-contrib-message-aggregator  
RUN npm install -g pm2  
RUN npm install  
  
EXPOSE 1880  
# CMD ["node-red", "-s", "/src/data/settings.js"]  
CMD ["pm2", "start", "/usr/bin/node-red", "--no-daemon", "--node-args=\"--
harmony\"", "--", "-s", "/src/settings.js"]

