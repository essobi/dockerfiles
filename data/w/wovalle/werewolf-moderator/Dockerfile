FROM node:alpine  
  
ENV PROJECT_ROOT /home/node/app/  
RUN mkdir -p $PROJECT_ROOT  
  
WORKDIR $PROJECT_ROOT  
  
COPY package.json $PROJECT_ROOT  
  
RUN npm install  
  
COPY . .  
  
EXPOSE 3000  
CMD [ "npm","run", "build" ]  
CMD ["npm", "run", "now-start"]  

