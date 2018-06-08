FROM node:8-alpine  
  
COPY package.json yarn.lock ./  
RUN yarn  
  
COPY . .  
RUN yarn build  
  
EXPOSE 3000  
CMD ["yarn", "start"]  

