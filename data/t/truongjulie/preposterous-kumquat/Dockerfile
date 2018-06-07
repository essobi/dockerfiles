FROM nodesource/trusty:6.2.2  
RUN apt-get update && apt-get install -y wget  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.1.0/dockerize-linux-
amd64-v0.1.0.tar.gz  
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.1.0.tar.gz  
  
ADD package.json package.json  
RUN npm install  
RUN npm install forever -g  
RUN npm install webpack -g  
RUN npm install --only=dev  
ADD . .  
RUN chmod +x ./wait-for-it.sh  
RUN webpack  
  
CMD ["npm", "start"]  
  

