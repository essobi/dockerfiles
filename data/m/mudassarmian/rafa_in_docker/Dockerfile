FROM ubuntu:latest  
MAINTAINER Mudassar M  
  
#ENV BOTDIR=/home/RafaBot  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get install -y git build-essential nodejs npm sudo  
  
RUN ln -s `which nodejs` /usr/bin/node  
RUN npm install -g yo generator-hubot  
  
CMD mkdir -p /opt/Rafa  
WORKDIR /opt/Rafa  
  
RUN sudo chmod -R g+rwx /root /opt/Rafa  
  
RUN sudo yo hubot --adapter hipchat --defaults  
  

