FROM node:9-stretch  
WORKDIR /usr/src/haste-server  
COPY . .  
RUN npm install  
RUN npm rebuild  
RUN mkdir /data  
EXPOSE 7777  
CMD [ "node", "server.js" ]  

