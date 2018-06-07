# Dockerizing Scala and Java  
# Installs apt-transport-https and sbt  
FROM openjdk:8  
MAINTAINER R. Heusser <roland.heusser@sri.com>  
  
# Update  
RUN apt-get -qqy update  
  
# Installation  
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  
RUN apt-get update -y  
RUN apt-get install -y apt-transport-https sbt  
RUN sbt sbt-version  
  
# Define working directory  
WORKDIR /root  

