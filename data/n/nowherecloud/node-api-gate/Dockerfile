FROM node:alpine  
  
WORKDIR /srv  
  
COPY . /srv  
  
RUN npm install --production  
  
ENV MONGODB_URI=mongodb://mongo/nowhere \  
AMQP_URI=amqp://rabbitmq \  
MYSQL_USER=change-me \  
MYSQL_PASS=change-me \  
MYSQL_DB=nowhere \  
XAPI_PATH=192.168.255.254 \  
XAPI_PORT=443  
  
ENTRYPOINT ["npm", "start", "--production"]  

