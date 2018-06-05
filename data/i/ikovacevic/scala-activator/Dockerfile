FROM ikovacevic/java:oracle-jdk-8  
MAINTAINER Igor Kovacevic <igor.kovacevic@gmail.com>  
  
RUN apt-get update && apt-get install -y wget unzip  
  
ENV ACTIVATOR_VERSION 1.3.10  
ENV ACTIVATOR_HOME /usr/local/activator  
  
RUN \  
cd /tmp && \  
wget http://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \  
unzip typesafe-activator-$ACTIVATOR_VERSION.zip -d /usr/local && \  
ln -s /usr/local/activator-dist-$ACTIVATOR_VERSION /usr/local/activator && \  
ln -s /usr/local/activator/bin/activator /usr/local/bin/ && \  
rm typesafe-activator-$ACTIVATOR_VERSION.zip  

