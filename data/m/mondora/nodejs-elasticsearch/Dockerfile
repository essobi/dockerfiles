FROM node:7  
MAINTAINER Paolo Scanferla <paolo.scanferla@mondora.com>  
  
# Install java 8  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y openjdk-8-jre  
  
# Install elasticsearch (elasticsearch can't run as root, therefore  
# we need to create a user for it)  
RUN adduser --system elasticsearch  
RUN curl -L -O
https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.1.2.tar.gz  
RUN tar -xvf elasticsearch-5.1.2.tar.gz  
RUN mv elasticsearch-5.1.2 /home/elasticsearch/  
RUN chown -R elasticsearch /home/elasticsearch  
COPY start-elasticsearch.sh /usr/bin/start-elasticsearch.sh  

