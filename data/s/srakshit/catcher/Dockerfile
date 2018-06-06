FROM node:8.10.0  
WORKDIR /code  
  
#Only required for debugging  
RUN npm install -g yarn knex node-gyp  
  
COPY . /code  
  
EXPOSE 8080  
CMD ["yarn", "start"]  

