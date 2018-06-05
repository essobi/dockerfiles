FROM node:9.11.1  
WORKDIR /app  
COPY package.json package.json  
COPY package-lock.json package-lock.json  
COPY src src  
RUN npm install --only=production  
EXPOSE 80  
CMD ["npm", "start"]  

