FROM mhart/alpine-node:latest  
MAINTAINER Ueqt <ueqtxu@gmail.com>  
RUN apk update && apk upgrade && apk add git && adduser -D -S -s /bin/sh -h
/sinopia sinopia  
USER sinopia  
RUN git clone \--depth 1 https://github.com/ueqt/sinopia /sinopia  
ADD config.yaml /sinopia/config.yaml  
WORKDIR /sinopia  
RUN npm install --production && npm cache clean  
VOLUME /sinopia/storage  
EXPOSE 4873  
CMD ["./bin/sinopia"]  

