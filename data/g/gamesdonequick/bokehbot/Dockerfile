FROM node:6  
WORKDIR /usr/src/app  
COPY . /usr/src/app/  
VOLUME $HOME/letsencrypt/etc  
VOLUME $HOME/.credentials/  
RUN npm install --production  
  
# The command to run  
EXPOSE 22222  
CMD ["node", "index.js"]  

