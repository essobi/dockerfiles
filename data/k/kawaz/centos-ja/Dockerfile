FROM centos:centos7  
MAINTAINER Yoshiaki Kawazu <kawazzz@gmail.com>  
  
RUN \  
localedef -i ja_JP -f UTF-8 ja_JP.UTF-8 && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
ENV LANG ja_JP.UTF-8  

