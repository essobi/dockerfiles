FROM node:6.10.0-alpine  
  
ENV appdir /usr/src/app/  
RUN mkdir -p $appdir  
WORKDIR $appdir  
  
ADD package.json .  
RUN npm install --only=production  
  
ADD ./config/app ./config/app  
ADD ./lib ./lib  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  

