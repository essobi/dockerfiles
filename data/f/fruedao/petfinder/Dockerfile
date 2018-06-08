FROM node:argon  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Bundle app source  
COPY . /usr/src/app  
  
RUN npm -g install bower  
  
RUN npm install  
RUN bower install --allow-root  
  
EXPOSE 8080  
CMD [ "npm", "start" ]  
  
#docker run --rm -d -p 8080:8080 \  
#-e APP_DOMAIN=http://localhost \  
#-e DB_HOST=mongo \  
#-e DB_NAME=petfinder \  
#-e DB_PORT=27017 \  
#-e NODE_ENV=dev \  
#-e PORT=8080 \  
#-e OPENSHIFT_NODEJS_IP=0.0.0.0 \  
#--link mongo:mongo --name petfinder fruedao/petfinder

