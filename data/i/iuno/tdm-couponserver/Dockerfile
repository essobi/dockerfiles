FROM node:alpine  
RUN npm install pm2 -g  
RUN apk add --update openssl  
  
# Configure log rotate  
RUN pm2 install pm2-logrotate  
RUN pm2 set pm2-logrotate:retain 10  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
RUN mkdir -p /usr/src/db  
  
WORKDIR /usr/src/app  
  
# Bundle app source  
COPY . /usr/src/app  
  
# Install app dependencies  
RUN npm install  
  
VOLUME /usr/src/db  
  
EXPOSE 3010  
CMD [ "pm2-docker", "npm", "--", "start" ]  

