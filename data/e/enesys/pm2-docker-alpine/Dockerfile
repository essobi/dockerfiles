FROM node:8-alpine  
MAINTAINER Enesys  
  
RUN apk --update add gcc g++ make python tzdata && npm install pm2 -g && npm
install node-gyp -g && \  
cp /usr/share/zoneinfo/Europe/Paris /etc/localtime && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 3300 8080  
VOLUME ["/app"]  
  
WORKDIR /app  
  
# Start process.yml  
CMD echo $NODE_ENV $PROCESS_FILE && yarn install && pm2-docker start
$PROCESS_FILE \--env $NODE_ENV  

