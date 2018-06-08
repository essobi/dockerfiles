# Pull base image.  
FROM node:slim  
  
MAINTAINER Leelow <leo@loza.ch>  
  
# Sinopia Version / Path / Backup  
RUN apt-get update && \  
apt-get install -y git && \  
git clone \--depth 1 https://github.com/Leelow/sinopia.git && \  
cd sinopia && \  
npm install --production && \  
npm cache clean  
  
ADD /config.yaml /sinopia/config.yaml  
  
WORKDIR /sinopia  
VOLUME /sinopia  
  
EXPOSE 4873  
CMD ["./bin/sinopia"]  

