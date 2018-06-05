FROM node:8-alpine  
  
USER root  
  
RUN npm set progress=false && npm config set depth 0 && npm cache clean
--force  
  
WORKDIR /opt/app  
  
COPY package*.json ./  
  
RUN npm install  
  
ENV NODE_ENV=production  
  
COPY . .  
  
RUN npm run build  
RUN npm prune --production  
  
EXPOSE 80  
  
CMD [ "npm", "start" ]  

