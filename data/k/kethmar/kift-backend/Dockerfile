FROM node:6-alpine  
  
WORKDIR /src  
  
COPY . .  
RUN npm install  
RUN npm rebuild node-sass  
  
CMD ["npm", "run", "app"]

