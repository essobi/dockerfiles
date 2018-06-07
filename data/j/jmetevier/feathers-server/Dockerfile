FROM node  
WORKDIR /usr/src/app  
COPY package.json .  
RUN npm install  
COPY . .  
EXPOSE 3030 80 443  
CMD ["npm", "run", "dev"]  
  

