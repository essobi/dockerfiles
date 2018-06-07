# The base image on which this image is based  
FROM ubuntu:14.04  
MAINTAINER Morten Minke  
  
RUN apt-get -y install wget  
  
# Download mongodb, extract it, move it and cleanup like a good citizen!  
RUN wget -nv --no-cookies http://downloads.mongodb.org/linux/mongodb-
linux-x86_64-2.4.8.tgz -O /tmp/mongodb-linux-x86_84.tgz && \  
tar zxf /tmp/mongodb-linux-x86_84.tgz && \  
mv mongodb-* /opt/mongodb && \  
rm -rf /tmp/*  
  
# The following volumes should not be considered part of the image, but
contain runtime data.  
# For best usage, this volume should be mounted to a host directory upon
running the container.  
RUN mkdir -p /data/db  
VOLUME ["/data/db"]  
  
CMD ["/opt/mongodb/bin/mongod"]  

