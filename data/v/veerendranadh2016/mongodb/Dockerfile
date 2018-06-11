# version 0.1  
FROM ubuntu:14.04  
MAINTAINER Veerendra "veeru538@gmail.com"  
RUN apt-get -y update \  
&& apt-get install wget tar -y \  
&& rm -rf /var/lib/apt/lists/*  
ENV MONGO_DATA_DIR=/data/db  
ENV MONGO_MAJOR 3.0  
ENV MONGO_VERSION 3.0.4  
RUN cd / ;wget http://downloads.mongodb.org/linux/mongodb-
linux-x86_64-ubuntu1404-3.0.4.tgz && \  
tar -xzf mongodb-linux-x86_64-ubuntu1404-3.0.4.tgz && \  
rm -rf mongodb-linux-x86_64-ubuntu1404-3.0.4.tgz && \  
mv mongodb-linux-x86_64-ubuntu1404-3.0.4/bin/* /usr/bin/ && \  
rm -rf mongodb-linux-x86_64-ubuntu1404-3.0.4  
RUN mkdir -p /data/db /data/configdb  
ADD mykey /opt/mykey  
RUN chmod 600 /opt/mykey  
VOLUME /data/db /data/configdb  
EXPOSE 27018  
CMD ["mongod"]  

