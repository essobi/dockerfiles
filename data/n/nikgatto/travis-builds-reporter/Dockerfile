FROM node:alpine  
  
WORKDIR /app  
COPY . .  
  
RUN npm install --unsafe-perm  
  
# if args will be added in the start script  
CMD ["npm", "start"]  
  
# test this container using interactive shell  
# CMD ["sh"]  

