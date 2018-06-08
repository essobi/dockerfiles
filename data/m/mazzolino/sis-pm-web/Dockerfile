FROM node:4  
RUN apt-get update  
  
RUN apt-get -y install sispmctl  
  
RUN chmod u+s /usr/bin/sispmctl  
  
WORKDIR /home/node/app  
COPY package.json .  
RUN npm install  
COPY . .  
RUN chown -R node:node .  
USER node  
  
CMD ["npm", "start"]  
EXPOSE 2638  

