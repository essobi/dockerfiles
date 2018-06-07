FROM node:8-alpine  
ADD index.js package.json /opt/app/  
WORKDIR /opt/app  
RUN yarn install  
VOLUME /opt/app/config/  
EXPOSE 8080  
CMD [ "node", "/opt/app/index.js" ]  

