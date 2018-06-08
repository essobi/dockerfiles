FROM node:8  
WORKDIR /usr/src/app  
COPY package.json package-lock.json ./  
RUN npm install --quiet  
COPY . .  
EXPOSE 9090  
CMD [ "npm", "start" ]  

