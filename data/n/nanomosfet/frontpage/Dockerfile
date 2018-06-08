FROM node:9  
WORKDIR /home/node/app  
COPY . .  
  
RUN npm install  
RUN npm run gulp  
  
EXPOSE 3000  
CMD ["npm", "start"]

