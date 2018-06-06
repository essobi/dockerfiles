FROM node:8  
WORKDIR /app  
COPY src/ /app  
COPY package.json /app  
COPY package-lock.json /app  
RUN npm install --production  
  
EXPOSE 3000  
ENTRYPOINT [ "node", "/app/index.js" ]  

