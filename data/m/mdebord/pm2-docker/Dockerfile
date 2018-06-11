FROM node:4-alpine  
  
LABEL maintainer="https://github.com/mdebord1"  
  
RUN npm install pm2 -g  
  
# Removed Keymetrics' volume tag...  
RUN mkdir /app  
  
WORKDIR /app  
  
CMD ["pm2-docker", "start", "--auto-exit", "--no-autorestart", "--env",
"production", "process.yml"]  

