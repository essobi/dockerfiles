FROM node:4  
COPY LICENSE LICENSE  
  
COPY package.json package.json  
RUN npm install --allow-root  
  
ENV API_HOST rubberduckapi  
ENV API_PORT 80  
ENV BOT_TOKEN 1234567890:abcde-fghijk  
  
COPY server.js server.js  
  
CMD ["node", "server.js"]

