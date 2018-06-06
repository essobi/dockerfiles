FROM systematicchaos/redis:latest  
MAINTAINER Javier Fernández-Bravo Peñuela <fraferp9@posgrado.upv.es>  
LABEL description="Raft: In search of an understandable consensus algorithm"  
  
RUN mkdir -p /home/cc-raft  
WORKDIR /home/cc-raft  
  
ADD . /home/cc-raft  
  
WORKDIR /home/cc-raft/raft  
RUN npm install && npm run build  
WORKDIR /home/cc-raft/raft-redis-server  
RUN npm install && npm run build  
WORKDIR /home/cc-raft/raft-redis-client  
RUN npm install && npm run build && cp dist/raft-redis-
client/raftRedisClient.js /home/cc-raft/  
  
WORKDIR /home/cc-raft/raft  
  
EXPOSE 6530/tcp  

