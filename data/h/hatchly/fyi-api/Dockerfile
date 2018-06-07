FROM node:alpine  
WORKDIR /app  
COPY ./ /app  
RUN npm install --production  
EXPOSE 8081  
CMD [ "node", "server.js" ]

