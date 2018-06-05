FROM node:9-alpine  
  
WORKDIR /app  
  
COPY ["package.json", "package-lock.json", "/app/"]  
  
RUN npm install -s --production  
  
CMD [ "npx", "speed-test" ]  

