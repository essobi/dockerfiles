FROM node:alpine  
  
RUN mkdir -p /srv/app  
WORKDIR /srv/app  
  
COPY package.json /srv/app/  
RUN npm install  
  
COPY server.js /srv/app  
  
EXPOSE 80  
CMD ["node", "server.js"]  

