#  
# Dockerfile for redis server  
#  
FROM centos:centos6  
  
# update system  
RUN rpm --import http://ftp.riken.jp/Linux/centos/RPM-GPG-KEY-CentOS-6  
RUN yum history new  
RUN yum update -y  
  
# install locale  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8  
  
# install epel repository  
RUN yum install -y http://ftp.riken.jp/Linux/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN rpm --import http://ftp.riken.jp/Linux/fedora/epel/RPM-GPG-KEY-EPEL-6  
  
# install redis  
RUN yum install -y redis  
  
EXPOSE 6379  
ENTRYPOINT ["/usr/sbin/redis-server"]  

