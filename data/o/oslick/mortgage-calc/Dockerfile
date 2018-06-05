FROM node  
  
MAINTAINER Andriy Shepitsen  
  
WORKDIR /usr/src/app  
  
COPY package*.json ./  
  
RUN npm i -g yarn  
  
COPY . .  
  
RUN yarn  
  
RUN yarn build  
  
EXPOSE 9000  
CMD [ "node", "server.js" ]  
  

