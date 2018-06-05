FROM node:7  
WORKDIR /srv  
  
EXPOSE 9000 9001 9002  
COPY package.json /srv/  
  
RUN npm install  
  
ADD server.js /srv/server.js  
  
CMD [ "npm", "start" ]

