FROM node  
  
WORKDIR /usr/src/app  
  
ADD . .  
  
RUN npm install && npm run build  
  
EXPOSE 8080  
CMD ["npm", "start"]  

