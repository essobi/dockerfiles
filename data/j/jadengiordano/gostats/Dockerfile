FROM node:carbon  
  
WORKDIR /usr/src/go-stats  
  
COPY package.json .  
RUN yarn install  
  
COPY . .  
  
EXPOSE 80  
CMD [ "yarn", "start" ]  

