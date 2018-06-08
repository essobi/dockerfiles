FROM mhart/alpine-node  
  
WORKDIR /var/www  
  
ADD index.js package.json /var/www/  
  
ENV PORT 80  
  
EXPOSE $PORT  
  
ENTRYPOINT npm start  

