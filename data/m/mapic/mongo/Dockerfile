FROM mongo:3.4.10  
MAINTAINER <knutole@mapic.io>  
  
# add start scripts  
RUN mkdir -p /mapic  
ADD mongod.conf /mapic/mongod.conf  
ADD init_mongo.js /mapic/init_mongo.js  
ADD mapic-entrypoint.sh /mapic/mapic-entrypoint.sh  
  
# start  
CMD ["bash", "/mapic/mapic-entrypoint.sh"]  

