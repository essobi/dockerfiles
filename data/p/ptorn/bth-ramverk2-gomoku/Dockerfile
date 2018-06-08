FROM node:alpine  
  
USER node  
RUN mkdir -p /home/node/app  
WORKDIR /home/node/app  
COPY package.json package-lock.json ./  
  
USER root  
COPY . .  
RUN chown -R node:node /home/node/app  
  
USER node  
ENV DBWEBB_WSSERVER=ptorn.se:4000  
RUN npm install  
  
EXPOSE 3000  

