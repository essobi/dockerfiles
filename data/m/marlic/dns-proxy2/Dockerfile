FROM node:boron  
  
RUN npm install -g dns-proxy2@1.0.5 && npm cache clean  
  
USER node  
WORKDIR /home/node  
  
EXPOSE 8053/udp  
  
CMD [ "dns-proxy", "--config", "conf.json" ]  

