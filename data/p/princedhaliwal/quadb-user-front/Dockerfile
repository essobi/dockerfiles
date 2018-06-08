FROM node:8.9.3  
WORKDIR /usr/src/app  
COPY . .  
RUN npm install  
RUN npm run build-all  
CMD node tools/server.js 3000  
EXPOSE 3000  

