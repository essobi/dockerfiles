#  
# CentOS Dockerfile  
#  
# Pull base image.  
FROM centos:latest  
MAINTAINER kayu28 "kayu28@gmail.com"  
RUN yum -y update  
RUN yum -y install rsync vim build-essential git  
RUN yum -y install java-1.7.0-openjdk  
RUN yum clean all  
RUN cp -p -f /usr/share/zoneinfo/Japan /etc/localtime  
  
ENV HOME /root  
WORKDIR /root  
  
CMD ["/bin/bash"]  

