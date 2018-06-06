FROM node:9.11.1-alpine as compiler  
  
WORKDIR /app  
  
COPY package.json ./  
  
RUN npm install --quiet --production  
  
COPY src ./src  
  
RUN npm run pkg  
  
FROM node:9.11.1-alpine  
  
COPY \--from=compiler /release/deployer /deployer  
  
CMD ["/deployer"]  

