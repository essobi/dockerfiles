FROM ubuntu:trusty  
  
MAINTAINER helphi  
  
ENV LANG=C.UTF-8 TZ=Asia/Shanghai  
  
RUN apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y net-tools curl vim && \  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  

