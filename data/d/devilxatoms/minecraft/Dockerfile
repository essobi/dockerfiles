FROM debian:latest  
MAINTAINER Brayan Caldera <ing.brayan.cm@gmail.com>  
  
USER root  
  
ENV EULA=true  
  
RUN apt-get update && apt-get install -y openjdk-8-jdk wget  
RUN mkdir /minecraft /data  
  
RUN wget -O /minecraft/craftbukkit-latest.jar
http://tcpr.ca/files/craftbukkit/craftbukkit-latest.jar  
  
WORKDIR /data  
  
ADD start-minecraft.sh /root/start-minecraft.sh  
ENTRYPOINT ["/bin/bash", "/root/start-minecraft.sh"]  
  
EXPOSE 25565  

