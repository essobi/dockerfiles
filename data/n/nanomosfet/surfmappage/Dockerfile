FROM node:9  
WORKDIR /home/node/app  
COPY . .  
  
RUN npm install  
RUN npm run build  
EXPOSE 80  
CMD ["npm", "start"]  

