FROM ubuntu:latest  
MAINTAINER Raphael Bottino <rbottino@id.uff.br>  
  
#Helios Master Install  
RUN apt-get update && apt-get install -y wget openjdk-7-jre  
RUN wget wget -q -O -
https://github.com/spotify/helios/releases/download/0.8.129/helios-debs.tar.gz
| tar -xzf - -C /opt  
RUN dpkg -i /opt/helios-services*.deb  
RUN dpkg -i /opt/helios-master*.deb  
  
#Helios Master Config  
ENV ZK_SERVER 172.17.42.1:2181  
COPY helios-master /etc/default/helios-master  
  
#Start Helios Master  
CMD helios-master --zk 172.17.42.1:2181  

