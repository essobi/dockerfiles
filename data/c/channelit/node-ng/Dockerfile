FROM ubuntu:16.04  
MAINTAINER hardikgw@gmail.com  
ENV\  
ENV=development  
RUN\  
apt-get update &&\  
apt-get install -y vim curl wget sudo default-jdk lsof git ntp &&\  
apt-get update &&\  
apt-get clean &&\  
apt-get -y upgrade  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs openssh-server  
RUN npm install -g watchman  
RUN npm install -g angular-cli  
RUN touch start.sh &&\  
echo "#!/usr/bin/env bash" >> start.sh &&\  
echo "ng serve --host 0.0.0.0 --port 4200" >> start.sh &&\  
chmod 755 start.sh  
EXPOSE 3000  

