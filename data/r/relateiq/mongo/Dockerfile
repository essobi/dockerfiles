FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y wget  
  
RUN mkdir -p /data/lucid_prod /data/local /logs /mongodb  
RUN wget --no-check-certificate --progress=dot:mega -O - https://s3-us-
west-1.amazonaws.com/relateiq-build-resources/mongodb-linux-x86_64-3.0.2.tgz |
tar -zx -C /mongodb --strip-components=1  
  
EXPOSE 27017 28017  
ADD mongo.conf /mongo.conf  
ADD rs-initiate.sh /rs-initiate.sh  
RUN /rs-initiate.sh  
  
CMD ["/mongodb/bin/mongod", "-f", "/mongo.conf"]  

