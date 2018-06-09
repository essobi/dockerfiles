FROM node:latest  
  
RUN npm install coin-hive-stratum  
RUN npm install respawn  
  
COPY monitor.js monitor.js  
  
EXPOSE 8892  
ENTRYPOINT node monitor.js  

