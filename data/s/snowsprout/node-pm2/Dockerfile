#docker build -t snowsprout/node-pm2 .  
FROM node:latest  
  
# Install PM2  
RUN npm install -g pm2  
WORKDIR /usr/src/apps  
  
CMD ["pm2-docker", "process.yml"]  
  
EXPOSE 26000

