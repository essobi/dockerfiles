FROM ubuntu:12.04  
MAINTAINER Arcus "http://arcus.io"  
RUN apt-get update  
RUN apt-get install -y make gcc wget  
RUN wget http://fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.4.9.tgz -O
/tmp/pkg.tar.gz  
RUN mkdir -p /data/db  
RUN ln -s /opt/mongodb/bin/mongo /usr/local/bin/mongo  
RUN ln -s /opt/mongodb/bin/mongod /usr/local/bin/mongod  
RUN (cd /tmp && tar zxf pkg.tar.gz && mv mongodb-* /opt/mongodb)  
RUN rm -rf /tmp/*  
EXPOSE 27017  
EXPOSE 28017  
CMD ["/opt/mongodb/bin/mongod", "--rest"]  

