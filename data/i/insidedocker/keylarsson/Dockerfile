FROM node:4.6  
# PM2 install  
RUN npm install pm2 -g  
  
# Copy, excluding .dockerignore.  
WORKDIR "/usr/src/"  
COPY . .  
RUN npm install  
  
# Run  
CMD pm2 start processes.json && pm2 logs  

