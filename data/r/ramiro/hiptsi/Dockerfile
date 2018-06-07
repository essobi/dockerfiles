FROM node:latest  
MAINTAINER Ramiro Berrelleza 'rberrelleza@gmail.com'  
COPY . /src  
RUN cd /src; npm install  
EXPOSE 5000  
CMD export MONGO_ENV=MONGO_URL; export
MONGO_URL="mongodb://$MONGO_PORT_27017_TCP_ADDR:27017/ac"; node --harmony
/src/web.js  

