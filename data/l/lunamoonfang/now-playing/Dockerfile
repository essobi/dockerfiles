FROM node:9  
ADD . /app  
  
WORKDIR /app  
  
RUN npm install  
  
RUN npm run build  
  
ENTRYPOINT ["npm", "run", "start"]  
  
EXPOSE 3000  

