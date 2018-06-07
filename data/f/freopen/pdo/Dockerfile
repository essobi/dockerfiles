FROM node:alpine  
WORKDIR /usr/src/app  
COPY . .  
RUN npm install  
RUN npm run build-client  
RUN npm run build-server  
EXPOSE 3000  
CMD npm run serve  

