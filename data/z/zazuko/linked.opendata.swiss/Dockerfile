FROM zazuko/trifid  
  
ADD config.json /usr/src/app/  
ADD package.json /usr/src/app/  
ADD views /usr/src/app/views  
  
CMD pm2-docker start npm -- start  
  
EXPOSE 8080  

