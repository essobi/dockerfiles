# Typesafe Activator for Ubuntu 14.04  
#  
# GitHub - http://github.com/dalekurt/docker-activator  
# Docker Hub - http://hub.docker.com/u/dalekurt/activator  
# Twitter - http://www.twitter.com/dalekurt  
FROM dalekurt/java7  
  
# Basic environment setup  
RUN apt-get update; apt-get install -y unzip wget  
  
MAINTAINER Dale-Kurt Murray "dalekurt.murray@gmail.com"  
ENV ACTIVATOR_VERSION 1.3.2  
RUN cd /tmp && \  
wget http://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION.zip && \  
unzip typesafe-activator-$ACTIVATOR_VERSION.zip && \  
mkdir /opt/typesafe && \  
mv /tmp/activator-$ACTIVATOR_VERSION
/opt/typesafe/activator-$ACTIVATOR_VERSION && \  
ln -s /opt/typesafe/activator-$ACTIVATOR_VERSION/activator
/usr/local/bin/activator && \  
rm /tmp/typesafe-activator-$ACTIVATOR_VERSION.zip  
  
EXPOSE 9000  
RUN mkdir /opt/app  
WORKDIR /opt/app  
CMD ["activator", "run"]  

