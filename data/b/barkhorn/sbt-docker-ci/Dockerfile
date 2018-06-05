  
FROM openjdk:8-alpine  
MAINTAINER Philipp Meyerhoefer (https://github.com/barkhorn)  
  
ENV SBT_VERSION 0.13.15  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
RUN apk add --update --no-cache --virtual=.dependencies tar wget bash  
RUN wget -qO- http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz |tar -xz -C /usr/local  
  
WORKDIR /app  

