FROM node:7.7.4-alpine  
RUN mkdir -p /data  
COPY ./src /data/src  
COPY ./package.json /data/  
WORKDIR /data  
RUN npm install --production  
EXPOSE 3005  
CMD [ "node", "src/main" ]  

