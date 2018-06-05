FROM node:9.11.1-alpine  
  
WORKDIR /src  
ADD . .  
  
RUN npm install --quiet --loglevel=error --only=production  
  
EXPOSE 8080  
CMD ["npm", "run", "serve"]  

