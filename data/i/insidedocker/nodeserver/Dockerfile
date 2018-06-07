FROM ubuntu:16.04  
# System update  
RUN apt-get update -y && \  
apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs  
  
# PM2 install  
RUN npm install pm2 -g  
  
# Copy, excluding .dockerignore.  
WORKDIR "/usr/src/"  
COPY . .  
RUN npm install  
  
# Run  
CMD pm2 start processes.json && pm2 logs  

