FROM ubuntu:14.04  
MAINTAINER Mike Christof <mhristof@gmail.com>  
  
ENV VERSION 5.0.1  
ENV SHA1 b8139a51834f6c0ff90a7de1159c0b2162b86e7e  
  
RUN apt-get update && apt-get install wget -y && \  
wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-$VERSION-
linux-x86_64.tar.gz -O filebeat-$VERSION-x86_64.tar.gz && \  
openssl sha1 filebeat-$VERSION-x86_64.tar.gz | grep $SHA1 && \  
mkdir filebeat-$VERSION-x86_64 && \  
tar xvf filebeat-$VERSION-x86_64.tar.gz -C filebeat-$VERSION-x86_64/ --strip-
components=1 && \  
cp filebeat-$VERSION-x86_64/filebeat /filebeat && \  
cp filebeat-$VERSION-x86_64/filebeat.yml /filebeat.yml && \  
cp filebeat-$VERSION-x86_64/filebeat.template.json /filebeat.template.json &&
\  
rm -r filebeat-$VERSION-x86_64/ filebeat-$VERSION-x86_64.tar.gz && \  
apt-get remove wget -y && \  
apt-get autoremove -y  
  
ENTRYPOINT ["/filebeat", "-e"]  

