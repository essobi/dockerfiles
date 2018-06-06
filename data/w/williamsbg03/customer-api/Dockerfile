FROM node:6.6.0  
COPY package.json ./  
RUN npm install  
  
COPY ./ ./  
  
RUN npm prune --production  
  
CMD ["npm", "start"]  

