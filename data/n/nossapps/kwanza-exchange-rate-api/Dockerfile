FROM node  
  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app/  
RUN npm install && npm install -g nodemon  
  
COPY server.js /usr/src/app/  
  
EXPOSE 3004  
CMD ["npm", "start"]  
CMD ["node", "server.js"]  

