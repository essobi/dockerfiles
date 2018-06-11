FROM node:alpine  
LABEL authors="Angelo Agatino Nicolosi <angelonicolosi@yanchware.com>"  
WORKDIR /srv/yanchware.cms.usersms  
COPY package*.json ./  
RUN npm install --only=production  
COPY . .  
EXPOSE 8080  
CMD [ "npm", "start" ]  

