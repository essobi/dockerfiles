FROM node:10-alpine  
  
WORKDIR /discord-irc  
RUN npm install -g discord-irc  
COPY ./config.json .  
  
VOLUME /discord-irc  
  
ENV CONFIG_FILE="config.json"  
CMD ["discord-irc"]  

