FROM node:10.3.0-alpine  
  
MAINTAINER Lucas Teske <lucas@teske.com.br>  
  
RUN apk update && apk add python python-dev python3 make gcc g++ autoconf bash
icu-libs icu-dev  
  
RUN npm -g install yarn  
  
RUN mkdir -p /opt/ircredirect  
COPY . /opt/ircredirect  
  
WORKDIR /opt/ircredirect  
  
RUN yarn  
  
ENV irc_server "irc.freenode.com"  
ENV irc_channel "#ircredirect"  
ENV mqtt_server "mosquitto.mosquitto"  
ENV mqtt_topic "ircredirect"  
CMD node /opt/ircredirect/server.js

