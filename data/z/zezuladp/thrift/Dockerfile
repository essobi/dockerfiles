# Modified from https://registry.hub.docker.com/u/evarga/thrift/dockerfile/  
# This Dockerfile is used to build an image containing the Apache Thrift
framework. This image may be used  
FROM java:8-jdk  
MAINTAINER Dan Zezula <dan@writelab.com>  
  
RUN apt-get update --fix-missing  
RUN apt-get -y upgrade  
  
# Set the Thrift version number for this image.  
ENV THRIFT_VERSION 0.9.2  
# Set some auxiliary env. variables for later steps.  
ENV FILE_NAME thrift-$THRIFT_VERSION  
ENV SRC_URL
http://www.trieuvan.com/apache/thrift/$THRIFT_VERSION/$FILE_NAME.tar.gz  
  
# Download the matching tarball from the remote site and unpack it inside the
container.  
ADD $SRC_URL $FILE_NAME.tar.gz  
RUN tar zxf $FILE_NAME.tar.gz  
RUN rm $FILE_NAME.tar.gz  
RUN mv $FILE_NAME /usr/local  
  
# Install all necessary dependencies needed by Thrift.  
RUN apt-get install -y -f --force-yes libboost-dev libboost-test-dev libboost-
program-options-dev libevent-dev automake libtool flex bison pkg-config g++
libssl1.0.0 libssl-dev libglib2.0-dev  
RUN apt-get install -y make  
  
# Install OpenJDK 7 (latest version of it) and Ant  
RUN apt-get install -y ant  
  
# Compile and install Thrift.  
RUN cd /usr/local/$FILE_NAME && ./configure --without-tests && make && make
install  
  

