FROM centos:latest  
MAINTAINER lhcpig <lhcpig@qq.com>  
  
WORKDIR /  
RUN yum install -y wget unzip  
RUN wget https://github.com/letsencrypt/letsencrypt/archive/master.zip & unzip
master.zip & rm -f master.zip  
  
WORKDIR /letsencrypt-master  
RUN ./letsencrypt-auto -v  

