FROM docker.io/node:8-slim  
  
RUN mkdir -p /tmp/mysite/  
  
WORKDIR /src  
ADD package.json .  
RUN npm install  
ADD . .  
  
EXPOSE 3000  
CMD ["node", "app.js"]  
  

