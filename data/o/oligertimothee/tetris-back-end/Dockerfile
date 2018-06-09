FROM keymetrics/pm2:latest  
  
LABEL maintainer="Oliger Timothee"  
  
ADD app ./app  
  
ENTRYPOINT cd /app && npm i && pm2-dev start app.js  
  
EXPOSE 8081  

