FROM ubuntu:16.04  
MAINTAINER Anastasia Zolochevska <anastasiia.zolochevska@gmail.com>  
  
WORKDIR /app  
ADD . /app  
  
RUN apt-get update  
RUN apt-get -y install nodejs  
RUN apt-get -y install npm  
  
RUN npm install  
ADD . /app  
  
ENV PORT=3000  
EXPOSE 3000  
ENTRYPOINT ["nodejs", "server.js"]  

