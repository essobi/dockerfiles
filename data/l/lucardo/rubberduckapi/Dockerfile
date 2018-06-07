FROM node:4  
COPY LICENSE LICENSE  
  
COPY package.json package.json  
RUN npm install --allow-root  
  
ENV PORT 80  
ENV MONGO_HOST mongodb  
ENV MONGO_PORT 27017  
ENV MONGO_DB skein  
  
COPY libs/ libs/  
COPY server.js server.js  
  
CMD ["node", "server.js"]

