FROM node:6  
WORKDIR /usr/src/app  
  
# first only copy package.json & install deps, s.t. this layer does not have
to be rebuilt every time we rebuild the image  
COPY package.json .  
RUN npm install  
  
COPY . .  
COPY .env.example .env  
  
ENV PORT 5000  
EXPOSE 5000  
CMD ["npm", "start"]  
  

