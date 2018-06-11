#Download base ubuntu image  
FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get -y install ca-certificates curl && \  
apt-get -y install build-essential net-tools git sudo socat wget  
  
RUN echo "ALL ALL=NOPASSWD: ALL" >> /etc/sudoers  

