FROM node:7  
RUN apt-get update; apt-get install -y redis-server  
USER node  
WORKDIR /home/node  
COPY wotcher wotcher  
USER root  
WORKDIR /home/node/wotcher  
CMD service redis-server start; /home/node/wotcher/bin/hubot -a discourse-
adapter  

