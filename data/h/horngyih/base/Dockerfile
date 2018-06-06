FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common apt-utils tzdata locales
wget vim  
RUN ln -fs /usr/share/zoneinfo/Asia/Kuala_Lumpur /etc/localtime  
RUN dpkg-reconfigure --frontend noninteractive tzdata  

