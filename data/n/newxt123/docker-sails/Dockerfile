FROM node  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN npm -g install sails  
RUN npm install pm2@latest -g  
RUN npm install -g mocha  
RUN npm install -g bower  
  
EXPOSE 1337  
# CMD sails lift  

