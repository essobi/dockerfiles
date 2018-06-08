FROM ubuntu:trusty  
MAINTAINER gansteed <gansteed@gmail.com>  
  
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty main restricted universe
multiverse" > /etc/apt/sources.list && \  
echo "deb http://mirrors.163.com/ubuntu/ trusty-security main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted
universe multiverse" >> /etc/apt/sources.list && \  
echo "deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted
universe multiverse" >> /etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get -y upgrade  

