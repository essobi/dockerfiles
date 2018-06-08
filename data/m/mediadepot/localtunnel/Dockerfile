FROM node:7-alpine  
  
#Create localtunnel folder structure & set as volumes  
RUN mkdir -p /srv/localtunnel/app  
ADD src/ /srv/localtunnel/app/  
  
WORKDIR /srv/localtunnel/app  
  
RUN npm install  
  
CMD ["node","index.js"]  

