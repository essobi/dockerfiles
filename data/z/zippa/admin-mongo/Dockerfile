FROM node:alpine  
  
MAINTAINER zippa <mirko.pazienza@gmail.com>  
  
RUN apk update && apk upgrade && \  
apk add --no-cache bash git openssh && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /app/user  
#RUN chown -R node:node /app/user  
#USER node  
RUN git clone https://github.com/mrvautin/adminMongo.git . && \  
npm install --only=production  
  
ADD config /app/user/config  
  
RUN chmod -R 777 /app/user  
EXPOSE 1234  
  
CMD node app.js  

