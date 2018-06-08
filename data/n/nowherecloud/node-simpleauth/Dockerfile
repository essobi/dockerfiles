FROM node:alpine  
  
WORKDIR /srv  
  
COPY . /srv  
  
RUN npm install --production  
  
ENTRYPOINT ["npm", "start", "--production"]  

