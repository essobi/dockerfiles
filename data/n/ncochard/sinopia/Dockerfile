# Pull base image.  
FROM rnbwd/node-io:latest  
  
MAINTAINER RnbWd <dwisner6@gmail.com>  
  
# Sinopia Version / Path / Backup  
ENV version v1.4.0  
RUN npm install sinopia  
  
CMD ["./node_modules/bin/sinopia --config config.yaml"]  
  
EXPOSE 4873  
VOLUME /sinopia/storage  

