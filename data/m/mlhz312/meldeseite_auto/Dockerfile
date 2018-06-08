FROM node:carbon  
  
COPY package.json package-lock.json ./  
  
RUN npm install && mkdir /app && cp -R ./node_modules ./app  
  
WORKDIR /app  
  
COPY . /app  
  
EXPOSE 3000  
CMD ["npm", "start"]

