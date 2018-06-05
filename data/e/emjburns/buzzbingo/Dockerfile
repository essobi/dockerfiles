FROM node:alpine  
MAINTAINER emjeburns@gmail.com  
  
WORKDIR /src  
COPY package.json .  
RUN npm i  
  
COPY . .  
EXPOSE 3000  
CMD ["npm", "start"]  

