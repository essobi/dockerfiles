FROM ubuntu  
MAINTAINER Gamut Gurus Technologies  
RUN apt-get update  
RUN apt-get install -y openssh-server  
RUN apt-get install -y vim  
RUN apt-get install -y net-tools  
RUN useradd -m -d /home/gamut -s /bin/bash gamut  
RUN apt-get install sudo  
EXPOSE 80  
ENTRYPOINT service ssh restart && bash  

