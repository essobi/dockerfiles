FROM keymetrics/pm2:latest  
  
LABEL maintainer="Oliger Timothee"  
  
ADD app .  
  
ADD app/pm2.json .  
  
ADD app/package.json .  
  
ENTRYPOINT pm2-docker start pm2.json  
  
EXPOSE 8080  

