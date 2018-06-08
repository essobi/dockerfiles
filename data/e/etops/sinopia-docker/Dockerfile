# Pull base image.  
FROM node:5.9  
MAINTAINER RnbWd <dwisner6@gmail.com>  
  
# Sinopia Version / Path / Backup  
RUN git clone \--depth 1 https://github.com/rlidwka/sinopia.git  
WORKDIR /sinopia  
RUN npm install --production  
  
# Clean  
RUN npm cache clean  
  
RUN mkdir -p storage  
  
ADD config.yaml /sinopia/config.yaml  
  
CMD ["./bin/sinopia"]  
  
EXPOSE 4873  
VOLUME /sinopia/storage

