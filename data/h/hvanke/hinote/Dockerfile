FROM node:6.11.2  
WORKDIR /app  
  
COPY . /app  
RUN npm install -g yarn && yarn --pure-lockfile  
  
EXPOSE 3000  
CMD ["npm", "run", "docker:start"]  

