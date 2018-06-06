FROM node:8.2.1  
WORKDIR /home/code/curriculum-api  
  
RUN npm i -g yarn  
  
COPY package.json .  
  
COPY yarn.lock .  
  
RUN yarn  
  
COPY . .  

