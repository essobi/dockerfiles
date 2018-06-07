FROM ubuntu:latest  
  
MAINTAINER Jiaqi Liu  
  
# Setup dependencies  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt update  
RUN apt upgrade -y  
RUN apt-get install lsb-release -y  
RUN apt-get install openjdk-8-jdk -y  
RUN apt-get install wget -y  
RUN apt-get install sudo -y  
  
# Install Drill  
RUN wget http://apache.mirrors.hoobly.com/drill/drill-1.13.0/apache-
drill-1.13.0.tar.gz  
RUN mkdir -p /opt/drill  
RUN tar -xvzf apache-drill-1.13.0.tar.gz -C /opt/drill  
  
ADD init.sh /etc/init.sh  
RUN chown root:root /etc/init.sh  
RUN chmod 700 /etc/init.sh  
ENV INIT /etc/init.sh  

