FROM node:alpine  
  
WORKDIR /srv  
  
COPY . /srv  
  
RUN npm install --development && npm run build && npm prune --production && rm
-rf assets  
  
EXPOSE 80  
ENTRYPOINT ["npm", "start", "--production"]  

