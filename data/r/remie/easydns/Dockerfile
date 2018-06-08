FROM node:latest  
  
WORKDIR /opt/easydns  
COPY package.json package.json  
COPY package-lock.json package-lock.json  
RUN npm install  
  
COPY index.js index.js  
  
EXPOSE 53/udp  
  
CMD ["npm", "start"]

