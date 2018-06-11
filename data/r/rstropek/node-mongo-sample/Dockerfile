FROM node:9 AS build  
WORKDIR /app  
COPY . .  
RUN npm install && npm run build  
RUN npm install --production  
  
FROM node:9-alpine  
WORKDIR /app  
COPY \--from=build /app/dist ./dist/  
COPY \--from=build /app/node_modules ./node_modules/  
ENV MONGO_URL=mongodb://mongo-server/member-management  
ENV port=80  
EXPOSE 80  
CMD ["node", "./dist/server.js"]  

